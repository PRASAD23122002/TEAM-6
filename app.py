import streamlit as st
from PIL import Image
from model import process_image


def main():
    st.title("Lungs Image Processing")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Process"):
            label,accuracy = process_image(image)
            st.write("Result:")
            st.write(label)
            st.write("confidence score")
            st.write(accuracy)
            if label=="adenocarcinoma\n":
                st.write("Cancer = Yes\n")
                st.write("Name = adenocarcinoma\n")
                st.write("Region = Adenocarcinomas of the lung are found in the outer region of the lung on glands that secrete mucus which  helps us breathe\n")
                st.write("Reason = passive smoke, environmental pollutants,family history\n")
                st.write("Symptoms = coughing, hoarseness, weight loss and weakness.")

            elif label == "large.cell.carcinoma\n":
                st.write("Cancer = Yes\n")
                st.write("Name = Large cell carcinoma\n")
                st.write("Region = Large-cell undifferentiated carcinoma lung cancer grows and spreads can be found anywhere in the lung\n")
                st.write("Reason = smoking, environmental pollutants,gentics\n")
                st.write("Symptoms = Persistent Cough,Shortness of Breath,Chest Pain.")

            elif label == "squamous.cell.carcinoma\n":
                st.write("Cancer = Yes\n")
                st.write("Name = Squamous cell carcinoma\n")
                st.write("Region = This type of lung cancer is found centrally in the lung,where the larger bronchi join the trachea to the lung,or in one of the main airway branches\n")
                st.write("Reason = Squamous cell lung cancer is generally linked to smoking\n")
                st.write("Symptoms = Coughing up blood,Hoarseness,Shortness of breath.")

            else:
                st.write("Type = Non Cancerous\n")




if __name__ == "__main__":
    main()
