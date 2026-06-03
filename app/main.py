import streamlit as st
from jinja2.exceptions import TemplateSyntaxError, TemplateError


from app.services.template_reader import read_template_file
from app.services.variable_extractor import extract_template_variables
from app.services.template_renderer import render_template
from app.services.form_validator import get_empty_required_fields
from app.services.filename_sanitizer import sanitize_filename

from app.ui.form_builder import build_dynamic_form
from app.ui.clipboard_button import display_copy_button


def main() -> None:
    st.set_page_config(
        page_title="DocuForge",
        page_icon="📄",
        layout="centered",
    )

    st.title("DocuForge")
    st.subheader("Génération documentaire à partir de templates dynamiques")

    st.write(
        "Cette première version permettra de charger un template Jinja2, "
        "de détecter ses variables, puis de générer un document final."
    )

    uploaded_file = st.file_uploader(
        "Uploader un template",
        type=["txt", "md"],
    )

    if uploaded_file is not None:
        try:
            content = read_template_file(uploaded_file)
            variables = extract_template_variables(content)
            output_filename = st.text_input(
                label="Nom du fichier généré",
                value="document_genere",
                key="output_filename",
            )

            st.success("Template chargé avec succès.")

            st.text_area(
                "Contenu du template",
                value=content,
                height=300,
            )

            st.write("Variables détectées :")

            if variables:
                st.code(", ".join(variables))

                form_values = build_dynamic_form(variables)

                if st.button("Générer le document"):
                    empty_fields = get_empty_required_fields(form_values)

                    if empty_fields:
                        st.warning(
                            "Certains champs obligatoires sont vides : "
                            + ", ".join(empty_fields)
                        )
                    else:
                        rendered_document = render_template(content, form_values)
                        safe_filename = sanitize_filename(output_filename)

                        st.subheader("Document généré")

                        st.text_area(
                            "Résultat",
                            value=rendered_document,
                            height=300,
                        )

                        display_copy_button(rendered_document)
                        
                        st.download_button(
                            label="Télécharger le document",
                            data=rendered_document,
                            file_name=f"{safe_filename}.txt",
                            mime="text/plain",
                        )
            else:
                    st.info("Aucune variable Jinja2 détectée dans ce template.")

        except UnicodeDecodeError:
            st.error("Impossible de lire ce fichier. Vérifie qu'il est encodé en UTF-8.")

        except TemplateSyntaxError as error:
            st.error(f"Erreur de syntaxe Jinja2 : {error}")
        
        except TemplateError as error:
            st.error(f"Erreur lors du rendu du template : {error}")

        except ValueError as error:
            st.error(str(error))


if __name__ == "__main__":
    main()