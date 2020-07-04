import streamlit as st
from pages.fetch import*

def main():
	## Title and description 
	# html_temp = """
	# 	<div style="background-color:blue;padding:10px">
	# 	<h1 style="color:white;text-align:center;">Streamlit NLP App </h1>
	# 	</div>
	# """
    #st.markdown(html_temp,unsafe_allow_html=True)
	front_up()
	# st.title('NLPJenny')
	# st.subheader("Natural Language Processing On the Go...")
	st.markdown("""
			
			 This is a Natural Language Processing(NLP) Based App useful for basic NLP task
			implemented using State of he Art API's on Streamlit Framework
			""")
	### features

	st.header('Features')

	st.markdown("""
			#### Basic NLP Taks:
			+ App covers the most basic NLP task of tokenisation, parts of speech tagging.
				You can paste the desired content or may directly pass the url for the text.
			#### Named Entity Recognition and Topic Modelling:
			+ Named Entites like organistion person etc are recognised and top topics from the corpus
				are found based on LDA modelling.
			#### Machine Translations:
			+ Machine Translation, or aka Language Translation. Currently app is able to translate 10
				different Languages.
			
			#### Text Summarisation:
			+ It summerizes the given text into few lines. One can copy paste the article or may direclty
				pass the URL. (URL text scrapping is desinged according to wikipedia)
			
			#### Caption Generator:
			+ Capton Generator is a combination of computer vission as well as NLP. It generates a caption 
				for the uploaded image. It has options for different models to try out. It uses IBM api,
				Wiz wiz api as well as MS -COCO dataset model 
			""")
