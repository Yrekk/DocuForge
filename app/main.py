import streamlit as st

from app.constants import APP_MODES, AppMode, FormKeyPrefix
from app.controllers.offline_template_controller import run_offline_template_mode
from app.controllers.prompt_generator_controller import run_prompt_generator_mode


def main() -> None:
    st.set_page_config(
        page_title="DocuForge",
        page_icon="📄",
        layout="centered",
    )

    st.title("DocuForge")
    st.subheader("Génération documentaire à partir de templates dynamiques")

    selected_mode = st.radio(
        "Mode",
        APP_MODES,
        format_func=lambda mode: mode["label"],
    )

    selected_mode_value = selected_mode["value"]

    if selected_mode_value == AppMode.NONE:
        st.info("Sélectionnez un mode de génération pour commencer.")

    elif selected_mode_value == AppMode.OFFLINE:
        run_offline_template_mode(key_prefix=FormKeyPrefix.OFFLINE)

    elif selected_mode_value == AppMode.PROMPT:
      run_prompt_generator_mode(key_prefix=FormKeyPrefix.PROMPT)


if __name__ == "__main__":
    main()