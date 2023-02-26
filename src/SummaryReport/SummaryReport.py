import os
import sys
from datetime import datetime
import dominate
from dominate.tags import *
from robot.api import ExecutionResult, ResultVisitor
from styling import css



class SummaryReport(ResultVisitor):
    
    def __init__(self) -> None:

        self.title_doc = "Title is editable"
        self.title_disc = 'Documentation is also editable after exporting the report\nLorem ipsum ...'
        self.test_cases = []
        self.test_cases_status = []
        self.test_cases_start = []
        self.test_cases_ended = []
        self.fail_error_msg = []

    def visit_test(self, test):
        test_names = test.name
        test_status = test.status
        started_at = test.starttime
        ended_at = test.endtime
        error_msg = test.message
        self.test_cases.append(test_names)
        self.test_cases_status.append(test_status)
        self.fail_error_msg.append(error_msg)
        self.test_cases_start.append(self._format_robot_timestamp(started_at))
        self.test_cases_ended.append(self._format_robot_timestamp(ended_at))
        
        self.All_tests_count = len(self.test_cases)
        self.Passes = self.test_cases_status.count("PASS")
        self.Failes = self.test_cases_status.count("FAIL")
        self.Skipes = self.test_cases_status.count("SKIP")
        
        self.Passes_pec = round((self.Passes / self.All_tests_count)*100,2)
        self.Failes_pec = round((self.Failes / self.All_tests_count)*100,2)
        self.Skipes_pec = round((self.Skipes / self.All_tests_count)*100,2)
        now = datetime.now()
        self.dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        self.generate_html()

    def _format_robot_timestamp(self, timestamp):
        dt = datetime.strptime(timestamp,'%Y%m%d %H:%M:%S.%f')
        tt = dt.strftime('%H:%M:%S.%f')
        return tt

    def generate_html(self):
        doc = dominate.document(title="Repo-Reporting")
        
        with doc.head:
            link(rel='stylesheet', href='style.css')
           
        with doc:
            #style(css)
            with div(cls="container"):
                h1("Test Summary Report!")
                h3(self.title_doc,cls="edit")
                p(self.title_disc,cls="edit")
                button("Print",onclick="window.print()",cls="printer",id="printPageButton")
                for x in range(5):
                    br()
                div(f'{self.Passes_pec}%',cls="pie animate piepass")
                div(f'{self.Failes_pec}%',cls="pie animate piefail")
                div(f'{self.Skipes_pec}%',cls="pie animate pieskip")
                br()
                br()
                section("Pass Test cases ",self.Passes,cls="section")
                section("Fail Test cases ",self.Failes,cls="section")
                section("Skip Test cases ",self.Skipes,cls="section")
                section("Total Test cases ",self.All_tests_count,cls="section")
                with table(cls="content-table").add(tbody()):
                    with tr():
                        th("Test Case")
                        th("Msg")
                        th("Status")
                        th("Started")
                        th("Ended")
                    for x,z,y,s,e in zip (self.test_cases,self.fail_error_msg,self.test_cases_status,self.test_cases_start,self.test_cases_ended):
                        tr()
                        td(x)
                        td(z)
                        if y == "PASS":
                            td(span(y,cls="label Pass"))
                        if y == "SKIP":
                            td(span(y,cls="label Skip"))
                        if y == "FAIL":
                            td(samp(y,cls="label Fail"))
                        td(s)
                        td(e)
                div(self.dt_string,cls="dt_time")
        
        if not os.path.exists("Test_results"):
            os.makedirs("Test_results")

        with open("Test_results/Summary.html", "w+") as file:
            file.write(doc.render())

        with open("Test_results/style.css", "w") as file:
            file.write(css)
        
    
if __name__ == "__main__":
    original_output_xml = sys.argv[1]
    if not os.path.isfile(original_output_xml):
        raise FileNotFoundError(f'{original_output_xml} is not a valie xml path')
    result = ExecutionResult(original_output_xml)
    result.visit(SummaryReport())
