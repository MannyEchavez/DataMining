from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import pandas as panda
import matplotlib.pyplot as plot

def associations_location_diagnosis_and_demographics():

    location_diagnosis_demographic_matrix = get_matrix_of_location_diagnosis_and_demographics()

    boolean_converter = TransactionEncoder()

    data_converted_to_boolean = boolean_converter.fit(location_diagnosis_demographic_matrix).transform(location_diagnosis_demographic_matrix)

    dataframe_of_booleans = panda.DataFrame(data_converted_to_boolean, columns = boolean_converter.columns_)

    alzheimers_associations = apriori(dataframe_of_booleans, use_colnames = True, min_support = 0.02)

    alzheimers_associations['itemsets'] = alzheimers_associations['itemsets'].apply(lambda t: ', '.join(list(t))).astype('unicode')

    plot_alzheimers_associations_as_bar_chart(alzheimers_associations)

    #If this code is ran on a different computer, the path must be changed to a path that is relevant to the different computer.
    alzheimers_associations.to_csv(r"C:\Users\Deriv\PycharmProjects\AssociationMiningFinalProject\Alzheimers Associations.csv", index = False)

def plot_alzheimers_associations_as_bar_chart(alzheimers_associations):

    associations = alzheimers_associations['itemsets']

    support = alzheimers_associations['support']

    plot.barh(associations, support, color = "green")

    plot.title("Lifestyle factors, demographics, and geographic locations associated with Alzheimer's Disease")

    plot.ylabel('Association')

    plot.xlabel('Support')

    plot.legend(["Association"])

    plot.show()

def get_matrix_of_location_diagnosis_and_demographics():

    # IMPORTANT PREPROCESSING STEP. If this code is ran with the original Alzheimer's disease excel file.
    # As a preprocessing step, I removed the commas from inside of the qoutes in the CSV file by using an excel command so I can freely split the CSV by comma.

    with open("Alzheimer_s_Disease_and_Healthy_Aging_Data.csv") as unprocessed_data:

        # Discarding the header
        unprocessed_data.readline()

        location_diagnosis_demographic_matrix = []

        for line in unprocessed_data:
            row_in_unprocessed_data = line.split(",")

            inner_list = [row_in_unprocessed_data[4], row_in_unprocessed_data[7], row_in_unprocessed_data[23]]

            remove_empty_strings(inner_list)

            location_diagnosis_demographic_matrix.append(inner_list)

        return location_diagnosis_demographic_matrix

# There are empty strings inside some Strings in the CSV file.
# The output looks better with them gone.
def remove_empty_strings(inner_list):

    for t in range(len(inner_list)):
        if (inner_list[t] == ""):
            inner_list.pop(t)
            t = t - 1

if __name__ == '__main__':
    associations_location_diagnosis_and_demographics()