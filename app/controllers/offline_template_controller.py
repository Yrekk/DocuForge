import streamlit as st
from jinja2.exceptions import TemplateError, TemplateSyntaxError

from app.services.template_reader import read_template_file
from app.workflows.template_generation_workflow import run_template_generation_workflow


def run_offline_template_mode(key_prefix: str) -> None:
    """
    Run the offline document generation workflow.

    This mode lets the user upload a Jinja2 template, fill detected variables,
    generate the final document, copy it, and download it.
    """
    st.subheader("Génération documentaire offline")

    st.write(
        "Chargez un template Jinja2, remplissez les champs détectés, "
        "puis générez le document final."
    )

    uploaded_file = st.file_uploader(
        "Uploader un template",
        type=["txt", "md"],
    )

    if uploaded_file is not None:
        try:
            template_content = read_template_file(uploaded_file)

            st.success("Template chargé avec succès.")

            st.text_area(
                "Contenu du template",
                value=template_content,
                height=300,
            )

            output_filename = st.text_input(
                label="Nom du fichier généré",
                value="document_genere",
                key="offline_output_filename",
            )

            run_template_generation_workflow(
                template_content=template_content,
                key_prefix=key_prefix,
                generate_button_label="Générer le document",
                generate_button_key="generate_offline_document",
                result_title="Document généré",
                result_area_label="Résultat",
                copy_button_label="Copier le résultat",
                result_height=300,
                enable_download=True,
                download_filename=output_filename,
            )

        except UnicodeDecodeError:
            st.error("Impossible de lire ce fichier. Vérifie qu'il est encodé en UTF-8.")

        except TemplateSyntaxError as error:
            st.error(f"Erreur de syntaxe Jinja2 : {error}")

        except TemplateError as error:
            st.error(f"Erreur lors du rendu du template : {error}")

        except ValueError as error:
            st.error(str(error))