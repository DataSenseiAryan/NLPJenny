
import re
import streamlit as st
from pages.fetch import *
import sys
from gensim.summarization.summarizer import summarize
# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import spacy
#from summarizer import Summarizer as sz




def main():
	# Title
	front_up()

	st.title('Text Summarization')
	 
	if st.checkbox('Extractive Text Summarisation', key='ts'):
		st.subheader('Summary based on Extraction')
		summary_options = st.selectbox("Choose Summarizer", ['sumy', 'gensim'])
		boool, text = selection(key='ts')

		if st.button("Summarize", key='ts'):
			if boool == 0:
				message = text
				summarizevis(message, summary_options)

				#st.json(nlp_result)

			else:
				try:
					message = get_text(text)
					summarizevis(message, summary_options)
					#st.json(nlp_result)
				except BaseException as e:
					st.warning(e)

	if st.checkbox('Abstractive Text Summarization', key='ats'):
		st.subheader('Abtract Generation')

		boool, text = selection(key='ats')

		if st.button("Summarize", key='ats'):
			if boool == 0:
				message = text
				bert_sum(message)

			else:
				try:
					message = get_text(text)
					bert_sum(message)

				except BaseException as e:
					st.warning(e)
