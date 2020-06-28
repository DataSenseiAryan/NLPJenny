"""Main module for the streamlit NLPJenny app"""
import streamlit as st


import pages.home
import pages.basicNLP
import pages.captionGenerator
import pages.nertm
import pages.machineTranlation
import pages.textSummarization

#ast.core.services.other.set_logging_format()

PAGES = {
    "Home": pages.home,
    "Basic NLP": pages.basicNLP,
    "NER and Topic MOdelling": pages.nertm,
    "Text Summarization": pages.textSummarization,
    "Machine Translation": pages.machineTranlation,
    "Caption Generator": pages.captionGenerator
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    #with st.spinner(f"Loading {selection} ..."):
        #ast.shared.components.write_page(page)
    # st.sidebar.title("Contribute")
    # st.sidebar.info(
    #     "This an open source project and you are very welcome to **contribute** your awesome "
    #     "comments, questions, resources and apps as "
    #     "[issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) of or "
    #     "[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) "
    #     "to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit). "
    # )
    st.sidebar.title("About App")
    st.sidebar.subheader("NLPJenny")
    st.sidebar.text("Natural Language Processing On the Go")
    st.sidebar.info(
        """
        This App uses State of the Art free tier API's from different paltforms
        like IBM,Google Cloud and libraries like Spacy,Genism, NLTK etc. It uses Streamlit
        for implemention of beatiful and easy web app.
        """
    )
    
    
    st.sidebar.title("Contact Developer")
    st.sidebar.info(
        """
        This app is develop by Aryan. You can learn more about me at
        [aryan chaudhary](https://aryanc55.github.io).
"""
    )
    
    st.sidebar.markdown("""  [Github](https://github/aryanc55)""") #change all thses three to  to iamge
    st.sidebar.markdown("""  [Twitter](https://github/aryanc55)""")
    st.sidebar.markdown("""  [Instagram](https://github/aryanc55)""")
    st.sidebar.markdown("""  [Medium](https://github/aryanc55)""")



    
    


if __name__ == "__main__":
    main()