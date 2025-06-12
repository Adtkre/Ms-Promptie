import customtkinter as ctk
import openai
import pyperclip

# OpenAI Setup
openai.api_key = "your-api-key"

def generate_prompt():
    user_input = entry.get("0.0", "end").strip()
    if not user_input:
        output_box.configure(state="normal")
        output_box.delete("0.0", "end")
        output_box.insert("0.0", "Enter something.")
        output_box.configure(state="disabled")
        return

    output_box.configure(state="normal")
    output_box.delete("0.0", "end")
    output_box.insert("0.0", "Generating...")
    output_box.update()

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You're a helpful prompt engineer."},
            {"role": "user", "content": f"Convert this into a clear, powerful prompt:\n{user_input}"}
        ]
    )
    prompt = response['choices'][0]['message']['content']

    output_box.delete("0.0", "end")
    output_box.insert("0.0", prompt)
    output_box.configure(state="disabled")

    copy_button.configure(command=lambda: pyperclip.copy(prompt))

# UI Setup
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("350x320+1000+100") 
app.title("Ms. Promptie")
app.configure(fg_color="#DEB7FF")
app.attributes("-topmost", 1)
app.resizable(False, False)

# Input Box 
input_shadow = ctk.CTkTextbox(app, height=80, width=300,  fg_color="#D9D9D9", text_color="#D9D9D9", corner_radius=6, border_width=0)
input_shadow.place(x=26, y=15)  
 
entry = ctk.CTkTextbox(app, height=80, width=300,  fg_color="#FFFFF5", text_color="#000000",  font=("Arial", 12), corner_radius=6, border_color="#C1A1E1", border_width=2)
entry.place(x=23, y=12)

# Generate Button
generate_button = ctk.CTkButton(
    app,
    text="Generate Prompt",
    command=generate_prompt,
    fg_color="#C296FC",
    hover_color="#B07DEB",
    text_color="#FFFFFF",
    corner_radius=8,
    border_color="#9B5DE5",
    border_width=2,
    font=("Arial Rounded MT Bold", 18, "bold"),
    width=200,
    height=40,
)

generate_button.place(x=75, y=105) 

# Output Box 
shadow_box = ctk.CTkTextbox(app, height=80, width=300,    fg_color="#D9D9D9", text_color="#D9D9D9",    corner_radius=6, border_width=0)
shadow_box.place(x=26, y=175)

output_box = ctk.CTkTextbox(app, height=80, width=300,   fg_color="#FFFFF5", text_color="#000000",  font=("Arial", 11), corner_radius=6,   border_color="#C1A1E1", border_width=2)
output_box.place(x=23, y=172)
output_box.configure(state="disabled")


copy_button = ctk.CTkButton(
    app,
    text="Copy",
    text_color="#FFFFFF",
    fg_color="#C296FC",
    hover_color="#B07DEB",
    corner_radius=8,
    border_color="#9B5DE5",
    border_width=2,
    font=("Arial Rounded MT Bold", 18, "bold"),
    width=100,
    height=40,
    command=lambda: None
)
copy_button.place(x=125, y=265)

app.mainloop()
