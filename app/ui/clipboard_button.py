import html
import json
import uuid

import streamlit as components


def display_copy_button(text_to_copy: str, button_label: str = "Copier le résultat") -> None:
    """
    Display a browser-side copy button for the provided text.

    Args:
        text_to_copy: The text that should be copied to the clipboard.
        button_label: The label displayed on the copy button.
    """
    button_id = f"copy_button_{uuid.uuid4().hex}"

    escaped_text = json.dumps(text_to_copy)
    escaped_label = json.dumps(button_label)
    safe_button_label = html.escape(button_label)

    components.iframe(
        f"""
        <button id="{button_id}" style="
            padding: 0.5rem 0.75rem;
            border-radius: 0.5rem;
            border: 1px solid rgba(250, 250, 250, 0.2);
            background-color: transparent;
            color: white;
            cursor: pointer;
            font-size: 0.9rem;
        ">
            {safe_button_label}
        </button>

        <script>
            const button = document.getElementById("{button_id}");

            button.addEventListener("click", async () => {{
                await navigator.clipboard.writeText({escaped_text});

                button.innerText = "Copié !";

                setTimeout(() => {{
                    button.innerText = {escaped_label};
                }}, 1500);
            }});
        </script>
        """,
        height=50,
    )