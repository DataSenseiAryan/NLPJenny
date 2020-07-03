# # Summarization
# 	if st.checkbox("Show Text Summarization"):
# 		st.subheader("Summarize Your Text")

# 		message = st.text_area("Enter Text","Type Here ..")
# 		summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
# 		if st.button("Summarize"):
# 			if summary_options == 'sumy':
# 				st.text("Using Sumy Summarizer ..")
# 				summary_result = sumy_summarizer(message)
# 			elif summary_options == 'gensim':
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(rawtext)
# 			else:
# 				st.warning("Using Default Summarizer")
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(rawtext)

		
# 			st.success(summary_result)
