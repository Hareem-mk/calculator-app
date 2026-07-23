import gradio as gr
import math
from datetime import datetime, timedelta

# 1. Initialize history lists globally
history = []
sci_history = []

# --- Standard Calculator Function ---
def standard_calculator(num1, operator, num2):
    result = None
    if operator == "+ (Addition)":
        result = num1 + num2
    elif operator == "- (Subtraction)":
        result = num1 - num2
    elif operator == "* (Multiplication)":
        result = num1 * num2
    elif operator == "/ (Division)":
        if num2 == 0:
            return "Error: Cannot divide by zero", "\n".join(history)
        result = num1 / num2
    elif operator == "% (Percentage)":
        result = num1 % num2
    elif operator == "sqrt (Square Root of first number)":
        if num1 < 0:
            return "Error: Cannot find square root of negative number", "\n".join(history)
        result = math.sqrt(num1)
    elif operator == "x^n (Power)":
        result = num1 ** num2
    elif operator == "cube (x^3)":
        result = num1 ** 3
    elif operator == "inverse (1/x)":
        if num1 == 0:
            return "Error: Cannot divide by zero", "\n".join(history)
        result = 1 / num1
    
    if result is not None:
        formatted_res = str(round(result, 10))
        op_symbol = operator.split(" ")[0]
        history.append(f"{num1} {op_symbol} {num2} = {formatted_res}")
        return formatted_res, "\n".join(history)
    return "", "\n".join(history)

# --- Scientific Calculator Function ---
def scientific_calculator(num, operation):
    try:
        result = None
        if operation == "sin (Sine)":
            result = math.sin(math.radians(num))
        elif operation == "cos (Cosine)":
            result = math.cos(math.radians(num))
        elif operation == "tan (Tangent)":
            result = math.tan(math.radians(num))
        elif operation == "asin (Inverse Sine)":
            if num < -1 or num > 1:
                return "Error: Value must be between -1 and 1", "\n".join(sci_history)
            result = math.degrees(math.asin(num))
        elif operation == "acos (Inverse Cosine)":
            if num < -1 or num > 1:
                return "Error: Value must be between -1 and 1", "\n".join(sci_history)
            result = math.degrees(math.acos(num))
        elif operation == "atan (Inverse Tangent)":
            result = math.degrees(math.atan(num))
        elif operation == "log (Log base 10)":
            if num <= 0:
                return "Error: Cannot calculate log of zero or negative number", "\n".join(sci_history)
            result = math.log10(num)
        elif operation == "ln (Natural Log)":
            if num <= 0:
                return "Error: Cannot calculate ln of zero or negative number", "\n".join(sci_history)
            result = math.log(num)
        elif operation == "exp (e^x)":
            result = math.exp(num)
        elif operation == "factorial":
            if num < 0 or num != int(num):
                return "Error: Factorial only works on positive whole numbers", "\n".join(sci_history)
            result = math.factorial(int(num))
        elif operation == "abs (Absolute Value)":
            result = abs(num)
        elif operation == "ceil (Round Up)":
            result = math.ceil(num)
        elif operation == "floor (Round Down)":
            result = math.floor(num)
        elif operation == "trunc (Remove Decimal)":
            result = math.trunc(num)
        elif operation == "pi (π x number)":
            result = math.pi * num
        elif operation == "Euler's Number (e)":
            result = math.e * num
        elif operation == "cube root (x^1/3)":
            if num < 0:
                result = -((-num) ** (1/3))
            else:
                result = num ** (1/3)
        elif operation == "deg to rad (Degrees to Radians)":
            result = math.radians(num)
        elif operation == "rad to deg (Radians to Degrees)":
            result = math.degrees(num)
        
        if result is not None:
            formatted_res = str(round(result, 10))
            op_label = operation.split(" ")[0]
            sci_history.append(f"{op_label}({num}) = {formatted_res}")
            return formatted_res, "\n".join(sci_history)
        return "", "\n".join(sci_history)
    except Exception as e:
        return f"Error: {str(e)}", "\n".join(sci_history)

# --- Date Calculator Function ---
def date_calculator(date1_str, date2_str, operation):
    try:
        if operation == "Days between two dates":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            d2 = datetime.strptime(date2_str, "%Y-%m-%d")
            diff = abs((d2 - d1).days)
            return f"{diff} days"

        elif operation == "Add days to date":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            days = int(date2_str)
            result = d1 + timedelta(days=days)
            return result.strftime("%Y-%m-%d")

        elif operation == "Subtract days from date":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            days = int(date2_str)
            result = d1 - timedelta(days=days)
            return result.strftime("%Y-%m-%d")

        elif operation == "Day of week":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            return days[d1.weekday()]

        elif operation == "Weeks between two dates":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            d2 = datetime.strptime(date2_str, "%Y-%m-%d")
            diff = abs((d2 - d1).days) // 7
            return f"{diff} weeks"

        elif operation == "Months between two dates":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            d2 = datetime.strptime(date2_str, "%Y-%m-%d")
            months = abs((d2.year - d1.year) * 12 + (d2.month - d1.month))
            return f"{months} months"

        elif operation == "Years between two dates":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            d2 = datetime.strptime(date2_str, "%Y-%m-%d")
            years = abs(d2.year - d1.year)
            return f"{years} years"

        elif operation == "Age calculator":
            d1 = datetime.strptime(date1_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - d1.year - ((today.month, today.day) < (d1.month, d1.day))
            return f"{age} years old"

    except Exception as e:
        return f"Error: {str(e)}"
    return ""

# --- Unit & Currency Converter Function ---
def converter(value, from_unit, to_unit, converter_type):
    try:
        value = float(value)

        if converter_type == "Length":
            to_meters = {
                "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
                "inch": 0.0254, "ft": 0.3048, "miles": 1609.344,
                "nautical miles": 1852.0
            }
            if from_unit not in to_meters or to_unit not in to_meters:
                return "Unit not supported for Length"
            meters = value * to_meters[from_unit]
            result = meters / to_meters[to_unit]
            return f"{value} {from_unit} = {round(result, 6)} {to_unit}"

        elif converter_type == "Volume":
            to_liters = {
                "m3": 1000.0, "ft3": 28.3168, "liters": 1.0,
                "gallons (US)": 3.78541, "gallons (UK)": 4.54609
            }
            if from_unit not in to_liters or to_unit not in to_liters:
                return "Unit not supported for Volume"
            liters = value * to_liters[from_unit]
            result = liters / to_liters[to_unit]
            return f"{value} {from_unit} = {round(result, 6)} {to_unit}"

        elif converter_type == "Currency":
            to_usd = {
                "USD": 1.0, "EUR": 1.08, "GBP": 1.27,
                "SAR": 0.267, "AED": 0.272, "PKR": 0.0036,
                "INR": 0.012, "JPY": 0.0067, "CAD": 0.74,
                "AUD": 0.65, "CNY": 0.14, "CHF": 1.11
            }
            if from_unit not in to_usd or to_unit not in to_usd:
                return "Currency not found"
            usd = value * to_usd[from_unit]
            result = usd / to_usd[to_unit]
            return f"{value} {from_unit} = {round(result, 4)} {to_unit}"

    except Exception as e:
        return f"Error: {str(e)}"
    return ""

# Dynamic unit choices updater for Converter Tab
def update_units(converter_type):
    if converter_type == "Length":
        units = ["mm", "cm", "m", "km", "inch", "ft", "miles", "nautical miles"]
        return gr.update(choices=units, value="m"), gr.update(choices=units, value="ft")
    elif converter_type == "Volume":
        units = ["m3", "ft3", "liters", "gallons (US)", "gallons (UK)"]
        return gr.update(choices=units, value="liters"), gr.update(choices=units, value="gallons (US)")
    elif converter_type == "Currency":
        units = ["USD", "EUR", "GBP", "SAR", "AED", "PKR", "INR", "JPY", "CAD", "AUD", "CNY", "CHF"]
        return gr.update(choices=units, value="USD"), gr.update(choices=units, value="EUR")

# --- Gradio Interface Build ---
with gr.Blocks(title="My Advanced Calculator") as app:
    gr.Markdown("# 🔢 My Advanced Calculator")
    gr.Markdown("---")
    
    # Tab 1: Standard Calculator
    with gr.Tab("Standard Calculator"):
        gr.Markdown("### Standard Calculator")
        with gr.Row():
            with gr.Column(scale=2):
                num1 = gr.Number(label="First Number", value=0)
                num2 = gr.Number(label="Second Number", value=0)
                operator = gr.Dropdown(
                    choices=[
                        "+ (Addition)", "- (Subtraction)", "* (Multiplication)", 
                        "/ (Division)", "% (Percentage)", "sqrt (Square Root of first number)", 
                        "cube (x^3)", "x^n (Power)", "inverse (1/x)"
                    ],
                    label="Select Operator", value="+ (Addition)"
                )
                calc_button = gr.Button("Calculate", variant="primary")
                std_result = gr.Textbox(label="Answer")
            with gr.Column(scale=1):
                std_history = gr.Textbox(label="Calculation History", lines=10, max_lines=15, interactive=False)
                
        calc_button.click(
            fn=standard_calculator,
            inputs=[num1, operator, num2],
            outputs=[std_result, std_history]
        )
   
    # Tab 2: Scientific Calculator
    with gr.Tab("Scientific Calculator"): 
        gr.Markdown("### Scientific Calculator")
        with gr.Row():
            with gr.Column(scale=2):
                sci_num = gr.Number(label="Enter Number", value=0)
                sci_operation = gr.Dropdown(
                    choices=[
                        "sin (Sine)", "cos (Cosine)", "tan (Tangent)", "asin (Inverse Sine)", 
                        "acos (Inverse Cosine)", "atan (Inverse Tangent)", "exp (e^x)", 
                        "pi (π x number)", "Euler's Number (e)", "ceil (Round Up)", 
                        "floor (Round Down)", "trunc (Remove Decimal)", "log (Log base 10)", 
                        "ln (Natural Log)", "factorial", "abs (Absolute Value)", 
                        "cube root (x^1/3)", "deg to rad (Degrees to Radians)", "rad to deg (Radians to Degrees)"
                    ],
                    label="Select Operation", value="sin (Sine)"
                )
                sci_button = gr.Button("Calculate", variant="primary")
                sci_result = gr.Textbox(label="Answer")
            with gr.Column(scale=1):
                sci_history_box = gr.Textbox(label="Calculation History", lines=10, max_lines=15, interactive=False)
                
        sci_button.click(
            fn=scientific_calculator,
            inputs=[sci_num, sci_operation],
            outputs=[sci_result, sci_history_box]
        )

    # Tab 3: Date Calculator
    with gr.Tab("Date Calculator"):
        gr.Markdown("### Date Calculator")
        gr.Markdown("Format: YYYY-MM-DD (example: 2025-01-15)")

        date_operation = gr.Dropdown(
            choices=[
                "Days between two dates",
                "Weeks between two dates",
                "Months between two dates",
                "Years between two dates",
                "Add days to date",
                "Subtract days from date",
                "Day of week",
                "Age calculator"
            ],
            label="Select Operation",
            value="Days between two dates"       
        )
        with gr.Row():
            date1 = gr.Textbox(label="Date 1 (YYYY-MM-DD)", placeholder="2025-01-01")
            date2 = gr.Textbox(label="Date 2 or Number of Days", placeholder="2025-12-31")
        
        date_button = gr.Button("Calculate", variant="primary")
        date_result = gr.Textbox(label="Answer")

        date_button.click(
            fn=date_calculator,
            inputs=[date1, date2, date_operation],
            outputs=date_result
        )

    # Tab 4: Converter
    with gr.Tab("Converter"):
        gr.Markdown("### Unit & Currency Converter")

        converter_type = gr.Radio(
            choices=["Length", "Volume", "Currency"],
            label="Select Converter Type",
            value="Length"
        )        

        value_input = gr.Number(label="Enter Value", value=1)

        with gr.Row():
            from_unit = gr.Dropdown(
                choices=["mm", "cm", "m", "km", "inch", "ft", "miles", "nautical miles"],
                label="From",
                value="m"
            )
            to_unit = gr.Dropdown(
                choices=["mm", "cm", "m", "km", "inch", "ft", "miles", "nautical miles"],
                label="To",
                value="ft"
            )

        # Update dropdown choices dynamically when converter type changes
        converter_type.change(
            fn=update_units,
            inputs=converter_type,
            outputs=[from_unit, to_unit]
        )

        convert_button = gr.Button("Convert", variant="primary")
        convert_result = gr.Textbox(label="Result")

        convert_button.click(
            fn=converter,
            inputs=[value_input, from_unit, to_unit, converter_type],
            outputs=convert_result
        )   

# Launch the app
app.launch(theme=gr.themes.Soft(), share=True)