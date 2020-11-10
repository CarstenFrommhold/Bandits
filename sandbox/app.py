import streamlit as st
from sandbox import SessionState

st.header("Expected Distributions of Bandits")

# Sidebar
st.sidebar.subheader("Select Options")
# prediction = st.sidebar.selectbox(
#     "Model", options=["Image Similarity", 'Color Similarity']
# )
td_no = st.sidebar.number_input(
    min_value=1, max_value=10, value=1, label="No"
)
go = st.sidebar.button("GO")
# slider_options = st.select_slider(1,10)


#counter = 0
#if go & (prediction == "Image Similarity"):
# if go:
#     counter += 1
#     st.subheader('works like a charm')
#     st.text(str(counter))

# inital_parameters = {
#     "mu": 0,
#     "sigma": 1
# }

# ss = SessionState.get(mu=0)

# time.sleep(1)
# ss.x +=1
# st.text(str(ss.x))

# with st.empty():
#     for seconds in range(60):
#         st.text("Distribution looks as follows:")
#         chart_data = pd.DataFrame(
#         np.random.randn(20, 3), columns=['a', 'b', 'c'])
#         st.line_chart(chart_data)
#         st.text("This overwrites the line chart =/")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")

# for seconds in range(10):
#
#     st.empty()
#     mu = ss.mu
#     st.text("Refresh... ")
#     st.text(str(mu))
#     ss.mu +=1
#     time.sleep(1)

# with st.empty() as st_e:
#     for seconds in range(60):
#         st_e.text("Distribution looks as follows:")
#         chart_data = pd.DataFrame(
#         np.random.randn(20, 3), columns=['a', 'b', 'c'])
#         st_e.line_chart(chart_data)
#         st_e.text("This overwrites the line chart =/")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")

# Note: st.empty() is a container

# # Solution?:
#
# iteration = 0
# chart_data = pd.DataFrame(
#         np.random.randn(20, 3), columns=['a', 'b', 'c'])
#
# st.text(f"We observe iteration {iteration}")
# st.line_chart(chart_data)
#
# for _ in range(60):
#
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 3), columns=['a', 'b', 'c'])
#     iteration +=1
#     time.sleep(1)


# Refreshing everytime a button is clicked
ss = SessionState.get(mu=0)
st.text("Refresh... ")
st.text(str(ss.mu))
ss.mu +=1
