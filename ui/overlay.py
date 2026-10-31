# ============================================================
#  OVERLAY — Enhanced neon-themed floating signal dashboard (v5)
#  Scrollable signal history log, expiry countdown,
#  signal format: "✅ 1 MIN UP" / "✅ 2 MIN DOWN"
# ============================================================

import tkinter as tk
from tkinter import font as tkfont
import sys
sys.path.insert(0, '.')
from core.signal_result import SignalResult, SignalGrade
from core.market_context import MarketContext, TrendState, VolatilityRegime, MarketRegime
from config import UI, TRADE
import time as _time


class SignalOverlay:
    """
    Enhanced compact neon-themed floating overlay.
    v5: scrollable signal history, expiry countdown,
        signal format: 1 MIN UP / 2 MIN DOWN
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QuantSignal")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.95)
        self.root.configure(bg="#08080e")

        # Compact height since signal log was removed
        W, H = 310, 310
        sw = self.root.winfo_screenwidth()
        self.root.geometry(f"{W}x{H}+{sw - W - 16}+{20}")

        # Dragging
        self.root.bind("<ButtonPress-1>", self._drag_start)
        self.root.bind("<B1-Motion>", self._drag_move)
        self._dx = self._dy = 0
        self._width = W

        # ── Fonts (all BOLD for readability) ──
        F = UI.font_family
        self.f_head  = tkfont.Font(family=F, size=9,  weight="bold")
        self.f_sig   = tkfont.Font(family=F, size=22, weight="bold")
        self.f_grade = tkfont.Font(family=F, size=10, weight="bold")
        self.f_label = tkfont.Font(family=F, size=9,  weight="bold")
        self.f_value = tkfont.Font(family=F, size=9,  weight="bold")
        self.f_small = tkfont.Font(family=F, size=8,  weight="bold")
        self.f_prob  = tkfont.Font(family=F, size=8,  weight="bold")
        self.f_tiny  = tkfont.Font(family=F, size=7,  weight="bold")
        self.f_pattern = tkfont.Font(family=F, size=8, weight="bold")

        BG  = "#08080e"
        PAN = "#10101a"
        self._BG = BG
        self._PAN = PAN

        # Signal history tracking
        self._signal_history = []
        self._flash_active = False
        self._expiry_end_time = 0    # timestamp when trade expiry ends
        self._countdown_after_id = None  # for countdown timer

        # ═══════════════════════════════════════
        #  HEADER BAR
        # ═══════════════════════════════════════
        hdr = tk.Frame(self.root, bg="#0e0e18", height=26)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        self.status_dot = tk.Label(hdr, text="●", font=self.f_small,
                                    fg="#00f0ff", bg="#0e0e18")
        self.status_dot.pack(side="left", padx=(8, 3))

        tk.Label(hdr, text="QUANT SIGNAL", font=self.f_head,
                 fg="#00f0ff", bg="#0e0e18").pack(side="left")

        # Asset label moved down to prevent overlap

        close_btn = tk.Label(hdr, text="✕", font=self.f_label,
                              fg="#666", bg="#0e0e18", cursor="hand2")
        close_btn.pack(side="right", padx=8)
        close_btn.bind("<Button-1>", lambda e: self.root.destroy())

        # RESET button
        self.reset_btn = tk.Label(hdr, text="⟳ RESET", font=self.f_small,
                                   fg="#ff00ff", bg="#0e0e18", cursor="hand2")
        self.reset_btn.pack(side="right", padx=(0, 4))
        self.reset_btn.bind("<Button-1>", lambda e: self._do_reset())
        self.reset_btn.bind("<Enter>", lambda e: self.reset_btn.config(fg="#ff66ff"))
        self.reset_btn.bind("<Leave>", lambda e: self.reset_btn.config(fg="#ff00ff"))

        self.on_reset = None

        # TIMEFRAME BUTTONS
        tf_frame = tk.Frame(hdr, bg="#0e0e18")
        tf_frame.pack(side="right", padx=(0, 10))

        self.tf_btns = {}
        for tf in ["1m", "2m", "3m", "5m"]:
            btn = tk.Label(tf_frame, text=tf.upper(), font=self.f_small,
                           fg="#777", bg="#0e0e18", cursor="hand2")
            btn.pack(side="left", padx=2)
            btn.bind("<Button-1>", lambda e, t=tf: self._set_timeframe(t))
            self.tf_btns[tf] = btn

        self.on_tf_change = None

        # Neon line (will flash on new signals)
        self.neon_line = tk.Frame(self.root, bg="#00f0ff", height=2)
        self.neon_line.pack(fill="x")

        # ═══════════════════════════════════════
        #  SIGNAL + GRADE + PATTERN
        # ═══════════════════════════════════════
        sig_frame = tk.Frame(self.root, bg=BG)
        sig_frame.pack(fill="x", pady=(4, 0))
        
        # Asset Name display (moved from header to avoid overlap)
        self.asset_var = tk.StringVar(value="")
        self.asset_lbl = tk.Label(sig_frame, textvariable=self.asset_var, font=self.f_small, fg="#bb86fc", bg=BG)
        self.asset_lbl.pack(pady=(0, 4))

        self.grade_var = tk.StringVar(value="")
        self.grade_lbl = tk.Label(sig_frame, textvariable=self.grade_var,
                                   font=self.f_grade, fg="#ffd700", bg=BG)
        self.grade_lbl.pack()

        self.signal_var = tk.StringVar(value="SCANNING")
        self.signal_lbl = tk.Label(sig_frame, textvariable=self.signal_var,
                                    font=self.f_sig, fg="#555", bg=BG)
        self.signal_lbl.pack(pady=(0, 0))

        # Pattern badge (NEW)
        self.pattern_var = tk.StringVar(value="")
        self.pattern_lbl = tk.Label(sig_frame, textvariable=self.pattern_var,
                                     font=self.f_pattern, fg="#bb86fc", bg=BG)
        self.pattern_lbl.pack()

        self.dur_var = tk.StringVar(value="")
        tk.Label(sig_frame, textvariable=self.dur_var, font=self.f_small,
                 fg="#999", bg=BG).pack()

        # ═══════════════════════════════════════
        #  CONFIDENCE BAR + PROBABILITIES
        # ═══════════════════════════════════════
        conf_frame = tk.Frame(self.root, bg=BG)
        conf_frame.pack(fill="x", padx=14, pady=(4, 0))

        self.bar_canvas = tk.Canvas(conf_frame, height=6, bg="#1a1a28",
                                     highlightthickness=0, bd=0)
        self.bar_canvas.pack(fill="x")

        prob_row = tk.Frame(self.root, bg=BG)
        prob_row.pack(fill="x", padx=14, pady=(2, 0))

        self.prob_up_var = tk.StringVar(value="UP 0%")
        self.prob_down_var = tk.StringVar(value="DN 0%")
        self.prob_nt_var = tk.StringVar(value="NT 100%")
        self.conf_var = tk.StringVar(value="0%")

        tk.Label(prob_row, textvariable=self.prob_up_var, font=self.f_prob,
                 fg="#00ff88", bg=BG).pack(side="left")
        tk.Label(prob_row, textvariable=self.prob_down_var, font=self.f_prob,
                 fg="#ff1744", bg=BG).pack(side="left", padx=(10, 0))
        tk.Label(prob_row, textvariable=self.conf_var, font=self.f_prob,
                 fg="#aaa", bg=BG).pack(side="right")
        tk.Label(prob_row, textvariable=self.prob_nt_var, font=self.f_prob,
                 fg="#666", bg=BG).pack(side="right", padx=(0, 10))

        # ═══════════════════════════════════════
        #  CONTEXT PANEL (compact grid)
        # ═══════════════════════════════════════
        panel = tk.Frame(self.root, bg=PAN, bd=0)
        panel.pack(fill="x", padx=10, pady=(4, 0))

        rows_data = [
            ("TREND",      "—"),
            ("STRUCTURE",  "—"),
            ("MARKET",     "—"),
            ("VOLATILITY", "—"),
            ("MOMENTUM",   "—"),
            ("ELDER-RAY",  "—"),
            ("TIMEFRAME",  TRADE.primary_timeframe.upper()),
        ]
        self.trend_var    = tk.StringVar(value="—")
        self.struct_var   = tk.StringVar(value="—")
        self.market_var   = tk.StringVar(value="—")
        self.vol_var      = tk.StringVar(value="—")
        self.mom_var      = tk.StringVar(value="—")
        self.elder_ray_var = tk.StringVar(value="—")
        self.tf_var       = tk.StringVar(value=TRADE.primary_timeframe.upper())

        vars_list = [self.trend_var, self.struct_var, self.market_var,
                     self.vol_var, self.mom_var, self.elder_ray_var, self.tf_var]
        self._value_labels = {}

        for i, (lbl_text, _) in enumerate(rows_data):
            row = tk.Frame(panel, bg=PAN)
            row.pack(fill="x", padx=8, pady=1)

            tk.Label(row, text=lbl_text, font=self.f_label,
                     fg="#777", bg=PAN).pack(side="left")
            val_lbl = tk.Label(row, textvariable=vars_list[i], font=self.f_value,
                                fg="#e0e0e0", bg=PAN)
            val_lbl.pack(side="right")
            self._value_labels[lbl_text] = val_lbl

        self.trend_lbl     = self._value_labels["TREND"]
        self.struct_lbl    = self._value_labels["STRUCTURE"]
        self.vol_lbl       = self._value_labels["VOLATILITY"]
        self.mom_lbl       = self._value_labels["MOMENTUM"]
        self.elder_ray_lbl = self._value_labels["ELDER-RAY"]

        # ═══════════════════════════════════════
        #  ENTRY FACTORS + RISK
        # ═══════════════════════════════════════
        tk.Frame(self.root, bg="#1a1a28", height=1).pack(fill="x", padx=10, pady=(3, 0))

        info_frame = tk.Frame(self.root, bg=BG)
        info_frame.pack(fill="x", padx=12, pady=(2, 0))

        self.reasons_var = tk.StringVar(value="Waiting for signal...")
        tk.Label(info_frame, textvariable=self.reasons_var, font=self.f_small,
                 fg="#bbb", bg=BG, wraplength=self._width - 30,
                 justify="left").pack(anchor="w")

        self.risk_var = tk.StringVar(value="")
        self.risk_lbl = tk.Label(info_frame, textvariable=self.risk_var,
                                  font=self.f_small, fg="#ff8c00", bg=BG,
                                  wraplength=self._width - 30, justify="left")
        self.risk_lbl.pack(anchor="w")

        # ═══════════════════════════════════════
        #  SIGNAL HISTORY — Removed to save space
        # ═══════════════════════════════════════

        # ═══════════════════════════════════════
        #  STATS BAR (bottom) + SCAN INFO
        # ═══════════════════════════════════════
        tk.Frame(self.root, bg="#ff00ff", height=1).pack(fill="x", side="bottom")
        stats_bar = tk.Frame(self.root, bg="#0e0e18", height=32)
        stats_bar.pack(fill="x", side="bottom")
        stats_bar.pack_propagate(False)

        self.stats_var = tk.StringVar(value="0 signals  |  Win —  |  Streak —")
        tk.Label(stats_bar, textvariable=self.stats_var, font=self.f_tiny,
                 fg="#777", bg="#0e0e18").pack(pady=(3, 0))

        # Scan info row
        self.scan_var = tk.StringVar(value="Scans: 0  |  Candles: 0")
        tk.Label(stats_bar, textvariable=self.scan_var, font=self.f_tiny,
                 fg="#444", bg="#0e0e18").pack()

    # ═══════════════════════════════════════════════
    #  PUBLIC UPDATE METHODS
    # ═══════════════════════════════════════════════

    def update_signal(self, result: SignalResult, ctx: MarketContext = None):
        try:
            self._update_direction(result)
            self._update_confidence(result)
            self._update_probabilities(result)
            self._update_reasons(result)
            self._update_pattern(result)
            if ctx:
                self._update_context(ctx)
            # Track history only for tradeable signals (A+/A)
            if result.is_tradeable:
                self._add_to_history(result)
                self._trigger_flash(result)
        except Exception as e:
            pass  # Overlay update error handled silently to prevent UI crashes

    def update_stats(self, stats: dict):
        try:
            total = stats.get('today_total', 0)
            rate = stats.get('today_rate', 0)
            streak = stats.get('streak', 0)
            s_type = stats.get('streak_type', '')
            fire = "🔥" if s_type == 'win' and streak >= 3 else ""
            self.stats_var.set(f"{total} sigs  |  {rate:.0f}% win  |  {streak}{s_type[0:1]} {fire}")
        except Exception as e:
            pass  # Overlay update error handled silently to prevent UI crashes

    def update_training_stats(self, total: int, wins: int, losses: int, ml_samples: int, pending: bool = False):
        try:
            rate = (wins / total * 100) if total > 0 else 0
            status = "Waiting for outcome..." if pending else "Scanning..."
            self.stats_var.set(f"TRAINING: {wins}W {losses}L ({rate:.0f}%) | Samples: {ml_samples}")
            self.scan_var.set(f"Status: {status}")
        except Exception:
            pass

    def update_timeframe(self, tf: str):
        self.tf_var.set(tf.upper())
        if hasattr(self, 'tf_btns'):
            for t, b in self.tf_btns.items():
                b.config(fg="#00f0ff" if t == tf else "#777")

    def update_scan_info(self, scans: int, candles: int, signals: int = 0):
        """Update scan count, candle count, and signal count."""
        try:
            self.scan_var.set(f"Scans: {scans}  |  Candles: {candles}  |  Signals: {signals}")
        except Exception:
            pass

    def set_scanning(self):
        self.signal_var.set("SCANNING")
        self.signal_lbl.config(fg="#555")
        self.grade_var.set("")
        self.dur_var.set("")
        self.pattern_var.set("")
        self.reasons_var.set("Scanning for chart...")

    def set_no_chart(self):
        self.signal_var.set("NO CHART")
        self.signal_lbl.config(fg="#ff4444")
        self.grade_var.set("")
        self.pattern_var.set("")
        self.reasons_var.set("Open Olymp Trade chart")

    # ═══════════════════════════════════════════════
    #  INTERNAL UPDATES
    # ═══════════════════════════════════════════════

    def _update_direction(self, result: SignalResult):
        if result.is_tradeable:
            d = result.direction
            expiry = result.expiry_minutes
            # Signal format: "✅ 1 MIN UP" / "✅ 2 MIN DOWN"
            self.signal_var.set(f"✅ {expiry} MIN {d}")

            color = "#00ff88" if d == "UP" else "#ff1744"
            self.signal_lbl.config(fg=color)

            grade = result.grade.value
            if result.grade == SignalGrade.A_PLUS:
                gc = "#ffd700"
            elif result.grade == SignalGrade.A:
                gc = "#00f0ff"
            else:
                gc = "#888888"
            self.grade_var.set(f"★ {grade} SETUP ★")
            self.grade_lbl.config(fg=gc)

            self.dur_var.set(f"Trade: {expiry} MIN  •  {TRADE.primary_timeframe.upper()} chart")

            # Freeze display for 5 seconds before starting next cycle to let user read the signal
            self._freeze_display_until = _time.time() + 5.0
        elif result.is_displayable:
            # Displayable but NOT tradeable (Grade B) — warn user, hide direction
            self.signal_var.set("⚠ WAIT")
            self.signal_lbl.config(fg="#ffaa00")  # amber

            grade = result.grade.value
            self.grade_var.set(f"Grade {grade} - Not tradeable")
            self.grade_lbl.config(fg="#888888")  # gray
            self.pattern_var.set("")

            if result.rejection_reasons:
                self.dur_var.set(result.rejection_reasons[0][:45])
            else:
                self.dur_var.set("Signal not strong enough to trade")

            self._freeze_display_until = _time.time() + 5.0
        else:
            # Cycle ended with no high-confidence signal — show clearly
            self.signal_var.set("NO TRADE")
            self.signal_lbl.config(fg="#ffaa00")  # amber/yellow
            self.grade_var.set("")
            self.pattern_var.set("")
            
            self._freeze_display_until = _time.time() + 5.0
            
            if result.rejection_reasons:
                self.dur_var.set(result.rejection_reasons[0][:45])
            else:
                self.dur_var.set("Market unclear — next cycle starting...")

    def _update_pattern(self, result: SignalResult):
        """Show detected pattern name as a badge."""
        if result.is_tradeable and result.reasons:
            # Show first pattern
            pattern_text = result.reasons[0]
            # Color based on direction
            color = "#66ffaa" if "UP" in pattern_text else "#ff6688"
            self.pattern_var.set(f"⟨ {pattern_text} ⟩")
            self.pattern_lbl.config(fg=color)
        elif result.reasons:
            self.pattern_var.set(result.reasons[0][:30])
            self.pattern_lbl.config(fg="#666")
        else:
            self.pattern_var.set("")

    def _update_confidence(self, result: SignalResult):
        conf = result.confidence
        self.conf_var.set(f"{conf:.0f}%")
        self.bar_canvas.update_idletasks()
        w = self.bar_canvas.winfo_width()
        fw = max(1, int(w * conf / 100))
        self.bar_canvas.delete("all")
        if result.is_displayable:
            # Color gradient based on confidence
            if conf >= 85:
                c = "#ffd700"  # gold for very high
            elif conf >= 70:
                c = "#00ff88" if result.direction == "UP" else "#ff1744"
            else:
                c = "#ffeb3b"  # yellow for moderate (Grade B)
        else:
            c = "#2a2a3a"
        self.bar_canvas.create_rectangle(0, 0, fw, 6, fill=c, outline="")

    def _update_probabilities(self, result: SignalResult):
        self.prob_up_var.set(f"UP {result.prob_up*100:.0f}%")
        self.prob_down_var.set(f"DN {result.prob_down*100:.0f}%")
        self.prob_nt_var.set(f"NT {result.prob_no_trade*100:.0f}%")

    def _update_reasons(self, result: SignalResult):
        if result.entry_factors:
            self.reasons_var.set(" • ".join(result.entry_factors[:3]))
        elif result.reasons:
            self.reasons_var.set(" • ".join(result.reasons[:3]))
        else:
            self.reasons_var.set("Analysing...")

        if result.risk_flags:
            self.risk_var.set("⚠ " + " • ".join(result.risk_flags[:2]))
        else:
            self.risk_var.set("")

    def _update_context(self, ctx: MarketContext):
        # Trend
        self.trend_var.set(ctx.trend_label)
        tc = {TrendState.STRONG_BULLISH: "#00ff88", TrendState.BULLISH: "#66bb6a",
              TrendState.SIDEWAYS: "#999", TrendState.BEARISH: "#ef5350",
              TrendState.STRONG_BEARISH: "#ff1744"}
        self.trend_lbl.config(fg=tc.get(ctx.trend_state, "#e0e0e0"))

        # Structure (NEW)
        self.struct_var.set(ctx.structure_state.value[:18])
        sc = {"Bullish": "#00ff88", "CHOCH Bullish": "#66ffaa", "BOS Bullish": "#66ffaa",
              "Bearish": "#ff1744", "CHOCH Bearish": "#ff6666", "BOS Bearish": "#ff6666",
              "Unclear": "#666"}
        struct_color = "#e0e0e0"
        for key, color in sc.items():
            if key in ctx.structure_state.value:
                struct_color = color
                break
        self.struct_lbl.config(fg=struct_color)

        # Market
        self.market_var.set(ctx.regime_label)

        # Volatility
        self.vol_var.set(ctx.volatility_regime.value)
        vc = {VolatilityRegime.EXPANDING: "#ff8c00", VolatilityRegime.NORMAL: "#00ff88",
              VolatilityRegime.COMPRESSING: "#ffeb3b", VolatilityRegime.COLLAPSED: "#ff1744"}
        self.vol_lbl.config(fg=vc.get(ctx.volatility_regime, "#e0e0e0"))

        # Momentum
        s = ctx.momentum_score
        if s > 0.3:
            self.mom_var.set(f"▲ Bull ({s:.2f})")
            self.mom_lbl.config(fg="#00ff88")
        elif s < -0.3:
            self.mom_var.set(f"▼ Bear ({s:.2f})")
            self.mom_lbl.config(fg="#ff1744")
        else:
            self.mom_var.set(f"● Flat ({s:.2f})")
            self.mom_lbl.config(fg="#999")

        # Elder-Ray Oscillator
        if hasattr(ctx, 'elder_ray_valid') and ctx.elder_ray_valid:
            er = ctx.elder_ray_score
            # Check for special conditions first
            if ctx.elder_ray_zero_cross_up:
                self.elder_ray_var.set("★★ ZERO-CROSS UP")
                self.elder_ray_lbl.config(fg="#ffd700")
            elif ctx.elder_ray_zero_cross_down:
                self.elder_ray_var.set("★★ ZERO-CROSS DN")
                self.elder_ray_lbl.config(fg="#ffd700")
            elif ctx.elder_ray_bulls_divergence:
                self.elder_ray_var.set("⚠ BEAR DIV")
                self.elder_ray_lbl.config(fg="#ff8c00")
            elif ctx.elder_ray_bears_divergence:
                self.elder_ray_var.set("⚠ BULL DIV")
                self.elder_ray_lbl.config(fg="#ff8c00")
            elif ctx.elder_ray_exhaustion:
                self.elder_ray_var.set("⊘ EXHAUST")
                self.elder_ray_lbl.config(fg="#666")
            elif er > 0.15:
                self.elder_ray_var.set(f"▲ BULL ({er:+.2f})")
                self.elder_ray_lbl.config(fg="#00ff88")
            elif er < -0.15:
                self.elder_ray_var.set(f"▼ BEAR ({er:+.2f})")
                self.elder_ray_lbl.config(fg="#ff1744")
            else:
                self.elder_ray_var.set(f"● NEUTRAL ({er:+.2f})")
                self.elder_ray_lbl.config(fg="#999")
        else:
            self.elder_ray_var.set("SW calc")
            self.elder_ray_lbl.config(fg="#555")

    # ─── SIGNAL HISTORY (Scrollable) ─────────────────
    def _add_to_history(self, result):
        entry = {
            'direction': result.direction,
            'confidence': result.confidence,
            'grade': result.grade.value,
            'time': _time.strftime('%H:%M:%S')
        }
        self._signal_history.insert(0, entry)
        self._signal_history = self._signal_history[:5]  # Keep last 5

    # ─── SIGNAL FLASH ANIMATION ──────────────────
    def _trigger_flash(self, result: SignalResult):
        """Flash the neon border when a new tradeable signal fires."""
        if not result.is_tradeable:
            return
        if self._flash_active:
            return
        self._flash_active = True
        flash_color = "#00ff88" if result.direction == "UP" else "#ff1744"

        # A+ gets gold flash
        if result.grade == SignalGrade.A_PLUS:
            flash_color = "#ffd700"

        def flash_step(count):
            if count <= 0:
                self.neon_line.config(bg="#00f0ff")
                self._flash_active = False
                return
            if count % 2 == 0:
                self.neon_line.config(bg=flash_color)
            else:
                self.neon_line.config(bg="#08080e")
            self.root.after(150, flash_step, count - 1)

        flash_step(6)  # 3 blinks

    # ─── RESET HANDLER ────────────────────────────
    def _do_reset(self):
        """Handle reset button click — clear caches and restart scanning."""
        self.reset_btn.config(fg="#ffffff")
        self.signal_var.set("RESETTING")
        self.signal_lbl.config(fg="#ff00ff")
        self.grade_var.set("")
        self.pattern_var.set("")
        self.dur_var.set("Clearing cache...")
        self.reasons_var.set("Deleting __pycache__ + clearing history...")
        self.risk_var.set("")

        self.prob_up_var.set("UP 0%")
        self.prob_down_var.set("DN 0%")
        self.prob_nt_var.set("NT 100%")
        self.conf_var.set("0%")
        self.bar_canvas.delete("all")

        self.trend_var.set("—")
        self.struct_var.set("—")
        self.market_var.set("—")
        self.vol_var.set("—")
        self.mom_var.set("—")

        # History cleared along with log UI

        if self.on_reset:
            self.on_reset()

        def _post_reset():
            self.reset_btn.config(fg="#ff00ff")
            self.signal_var.set("SCANNING")
            self.signal_lbl.config(fg="#555")
            self.dur_var.set("")
            self.reasons_var.set("Fresh scan in progress...")

        self.root.after(1000, _post_reset)

    def _set_timeframe(self, tf: str):
        """Handle timeframe button click."""
        if self.on_tf_change:
            self.on_tf_change(tf)
        for t, b in self.tf_btns.items():
            b.config(fg="#00f0ff" if t == tf else "#777")

    # ─── ANALYSIS CYCLE DISPLAY ─────────────────────────
    def set_analyzing(self, progress: float, progress_text: str, result=None):
        """Show continuous scanner status with real-time diagnostic reasons."""
        self.signal_var.set("SCANNING")
        self.signal_lbl.config(fg="#00f0ff")
        self.grade_var.set("")
        self.pattern_var.set("")
        self.dur_var.set(progress_text)

        if result is not None:
            # Display real-time quantitative metrics while scanning
            conf_str = f"{result.confidence:.1f}%"
            dir_str = result.direction if result.direction else "WAIT"
            self.conf_var.set(f"{dir_str} {conf_str}")
            self.prob_up_var.set(f"Conf: {getattr(result, 'confluence_count', 0)}/7")
            self.prob_down_var.set(f"Grade: {result.grade.value if hasattr(result.grade, 'value') else result.grade}")
            
            # Show exact reason why trade has not fired yet
            if hasattr(result, 'rejection_reasons') and result.rejection_reasons:
                reason = result.rejection_reasons[0]
                self.reasons_var.set(f"⏳ Waiting: {reason[:45]}")
            elif hasattr(result, 'risk_flags') and result.risk_flags:
                risk = result.risk_flags[0]
                self.reasons_var.set(f"🛡️ Protected: {risk[:45]}")
            else:
                self.reasons_var.set(f"📊 Analyzing: Confluence {getattr(result, 'confluence_count', 0)}/7 (Need 4/7)")
        else:
            self.reasons_var.set("Monitoring for high-confluence signals...")
            pct = int(progress * 100)
            self.conf_var.set(f"{pct}%")
            self.prob_up_var.set("UP --")
            self.prob_down_var.set("DN --")

        self.prob_nt_var.set("")

        # Animate progress bar
        self.bar_canvas.update_idletasks()
        w = self.bar_canvas.winfo_width()
        fw = max(1, int(w * progress))
        self.bar_canvas.delete("all")
        if progress < 0.5:
            c = "#ff00ff"
        elif progress < 0.85:
            c = "#bb44ff"
        else:
            c = "#00f0ff"
        self.bar_canvas.create_rectangle(0, 0, fw, 6, fill=c, outline="")

    def set_cooldown(self):
        """Show brief cooldown between cycles."""
        if hasattr(self, '_freeze_display_until') and _time.time() < self._freeze_display_until:
            return  # keep showing the signal or NO TRADE for 5 seconds

        self.signal_var.set("COOLDOWN")
        self.signal_lbl.config(fg="#ff8c00")
        self.grade_var.set("")
        self.pattern_var.set("")
        self.dur_var.set("Signal cooldown... scanning resumes shortly")
        self.reasons_var.set("")
        
    def set_reset_state(self, asset_name: str):
        """Show full reset alert when asset changes."""
        self.signal_var.set("ASSET CHANGED")
        self.signal_lbl.config(fg="#ff00ff")  # Magenta alert
        self.grade_var.set(f"[{asset_name}]")
        self.grade_lbl.config(fg="#ffffff")
        self.pattern_var.set("MEMORY WIPED")
        self.pattern_lbl.config(fg="#ff0000")
        self.dur_var.set("Starting fresh scan from zero...")
        self.reasons_var.set("")
        
        # Flash the progress bar red
        self.bar_canvas.delete("all")
        w = self.bar_canvas.winfo_width()
        self.bar_canvas.create_rectangle(0, 0, w, 6, fill="#ff0000", outline="")
        self.conf_var.set("RST")



    # ─── DRAGGING ────────────────────────────────
    def _drag_start(self, e):
        self._dx, self._dy = e.x, e.y

    def _drag_move(self, e):
        x = self.root.winfo_x() + e.x - self._dx
        y = self.root.winfo_y() + e.y - self._dy
        self.root.geometry(f"+{x}+{y}")

    def run(self):
        self.root.mainloop()
