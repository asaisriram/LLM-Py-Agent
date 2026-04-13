import customtkinter as ctk

class GeminiGui(ctk.CTk):
    def __init__(self, process_callback):
        super().__init__()
        self.process_callback = process_callback
        
        self.title("API Chat Agent")
        self.geometry("1000x700")

        # Grid layout: Sidebar (0) and Main (1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (Stats only) ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(self.sidebar, text="Token Stats", font=("Arial", 18, "bold")).grid(padx=20, pady=(30, 20))

        # Statistics Group (Aesthetic Alignment)
        self.stats_frame = ctk.CTkFrame(self.sidebar, corner_radius=10)
        self.stats_frame.grid(padx=15, pady=10, sticky="ew")
        
        def create_stat_row(parent, label_text, row):
            lbl = ctk.CTkLabel(parent, text=label_text, font=("Arial", 11))
            lbl.grid(row=row, column=0, padx=(12, 5), pady=8, sticky="w")
            val = ctk.CTkLabel(parent, text="0", font=("Consolas", 13, "bold"), text_color="#1f6aa5")
            val.grid(row=row, column=1, padx=(5, 12), pady=8, sticky="e")
            parent.grid_columnconfigure(0, weight=1)
            return val

        self.thought_val = create_stat_row(self.stats_frame, "Thought Tokens", 0)
        self.output_val = create_stat_row(self.stats_frame, "Output Tokens", 1)

        # --- MAIN VIEW ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1) # Input
        self.main_frame.grid_rowconfigure(3, weight=3) # Output gets more space

        # Multi-line Input
        ctk.CTkLabel(self.main_frame, text="Input Prompt", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0,5))
        self.input_text = ctk.CTkTextbox(self.main_frame, border_width=2)
        self.input_text.grid(row=1, column=0, sticky="nsew", pady=(0, 20))

        # Output Display
        ctk.CTkLabel(self.main_frame, text="API Response", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", pady=(0,5))
        self.output_display = ctk.CTkTextbox(self.main_frame, state="disabled", border_width=2)
        self.output_display.grid(row=3, column=0, sticky="nsew")

        # Action Button
        self.btn = ctk.CTkButton(self, text="GENERATE", height=45, font=("Arial", 14, "bold"), command=self.on_click)
        self.btn.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def on_click(self):
        prompt = self.input_text.get("1.0", "end-1c") 
        if not prompt.strip(): return

        # UI Visual feedback
        self.btn.configure(state="disabled", text="THINKING...")
        self.update()

        # Notice we no longer pass 'tokens' here since the bridge/callback 
        # will pull it from the YAML config automatically.
        result = self.process_callback(prompt)

        # Update UI
        self.output_display.configure(state="normal")
        self.output_display.delete("1.0", "end")
        self.output_display.insert("1.0", result['text'])
        self.output_display.configure(state="disabled")
        
        self.thought_val.configure(text=str(result['thought']))
        self.output_val.configure(text=str(result['output']))
        self.btn.configure(state="normal", text="GENERATE")