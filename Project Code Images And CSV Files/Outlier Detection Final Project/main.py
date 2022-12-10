
import pandas as panda
import matplotlib.pyplot as plot

def detect_outliers():

    patient_type_frequency_dictionary = get_patient_type_frequency_dictionary()

    patient_type_frequency_dictionary = dict(sorted(patient_type_frequency_dictionary.items(), reverse = True,
                                         key = lambda count: count[1]))

    patient_type_frequency_data_frame = panda.DataFrame(list(patient_type_frequency_dictionary.items()),
                                                        columns = ['Type Of Patient', 'Count'])

    create_patient_type_frequency_bar_graph(patient_type_frequency_data_frame)

    patient_type_frequency_data_frame.to_csv(r"C:\Users\Deriv\PycharmProjects\OutlierDetectionFinalProject\Frequency Of Types Of Patients.csv", index = False)

def create_patient_type_frequency_bar_graph(patient_type_frequency_data_frame):

    #For some reason, there is serious performance issues when I use the String labels as my x axis.
    type_of_patient = [g for g in range(0, patient_type_frequency_data_frame.shape[0])]

    count = patient_type_frequency_data_frame['Count']

    plot.bar(type_of_patient, count, color = "darkcyan")

    plot.xlabel("Type Of Patient")

    plot.ylabel("Count Of Patient Type")

    plot.title("Frequency Of The Types Of Patients")

    plot.tick_params(labelbottom = False, bottom = False)

    plot.legend(["Frequency Of Patient Type"])

    plot.show()

def get_patient_type_frequency_dictionary():

    # IMPORTANT PREPROCESSING STEP If this code is ran with the original Alzheimer's disease excel file.
    # As a preprocessing step, I removed the commas from inside of the qoutes in the CSV file by using an excel command so I can freely split the CSV by comma.

    with open("Alzheimer_s_Disease_and_Healthy_Aging_Data.csv") as unprocessed_data:

        # Discarding the header
        unprocessed_data.readline()

        patient_type_frequency_dictionary = {}

        for line in unprocessed_data:
            row_in_unprocessed_data = line.split(",")

            helper_list = [row_in_unprocessed_data[23], row_in_unprocessed_data[4], row_in_unprocessed_data[7]]

            patient_type = get_patient_type(helper_list)

            if patient_type in patient_type_frequency_dictionary:
                patient_type_frequency_dictionary[patient_type] = patient_type_frequency_dictionary[patient_type] + 1
            else:
                patient_type_frequency_dictionary[patient_type] = 1

        return patient_type_frequency_dictionary

def get_patient_type(helper_list):

    patient_type = ""

    for m in range (len(helper_list)):
        if helper_list[m] != "":
            patient_type = patient_type + helper_list[m]
            if m < len(helper_list) - 1:
                patient_type = patient_type + ", "

    return patient_type.replace('"', "")

if __name__ == '__main__':
    detect_outliers()