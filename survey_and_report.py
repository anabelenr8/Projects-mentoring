from .survey_report.report import Report, predetermined_answers

# Define survey answers
survey_answers = predetermined_answers

# Generate report based on survey answers
report = Report()
report.generate()  # Outputs report text which is generated based on survey answers
