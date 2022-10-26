import xml.etree.ElementTree as ET
from datetime import datetime
import dominate
from dominate.tags import *
import os
from robot.api.deco import library
import sys

css = """
  
}
th,
td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
    
}
table {
    border-collapse: collapse;
    /* border: 1px solid #bdc3c7; */
    width: 100%;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
    border-radius: 0.5em;
    
}
tr {
    transition: all .2s ease-in;
    cursor: pointer;
}
.edit{
    /* contenteditable:true; */
    -webkit-user-modify:read-write-plaintext-only;
    color: black;
    font-family: 'Courier New', Courier, monospace;
    
}
th, td {
text-align: left;
padding: 16px;
color: black;
}
th{
    border-bottom: 2px solid #aaa;
}
tr:nth-child(even) {
background-color: #f2f2f2;
}
body {
    padding: 20px;
    margin: 20;
    font-family: Arial, Helvetica, sans-serif;
    /* background-color: #202325; */
    background-color: rgb(255, 255, 255);
}
tr:hover {
    background-color: rgb(228, 226, 226);
    transform: scale(1);
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}
h1 {
    font-weight: 600;
    text-align: center;
    background-color: #009a91;
    color: white;
    padding: 10px 0px;
    border-radius: 15px;
    font-family: 'Courier New', Courier, monospace;
}
.label.Pass{
    background-color: #97bd61;
    color: #fff;
    font-weight: bold;
}
.label.Fail{
    background-color: #ce3e01;
    color: #fff;
    font-weight: bold;
    font-size:13px;
}
.label.Skip{
    background-color: #fed84f;
    color: #fff;
    font-weight: bold;  
    font-size:13px;
}
.label {
    text-align: center;
    padding: 2px 5px;
    font-size: 0.75em;
    letter-spacing: 1px;
    /* white-space: nowrap; */
    border-radius: 3px;
    padding: 10;
}
.SummNum{
    /* text-align: right; */
    font-size: 5ch;
    
    margin: 1%;
    padding: 1px;
    width: max-content;
    border: 1px solid blue;
    float: left;
    /* font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; */
    
}
.text_{
    width: max-content;
    float: left;
    border: 1px solid blue;
}
.pie {
    --p:100;
    --b:22px;
    /* --c:#97bd61; */
    --w:150px;
    
    width:var(--w);
    aspect-ratio:1;
    position:relative;
    display:inline-grid;
    margin:5px;
    place-content:center;
    font-size:25px;
    font-weight:bold;
    font-family:sans-serif;
    /* color: #37a98c; */
    color: black;
}
.pie:before,
.pie:after {
content:"";
position:absolute;
border-radius:50%;
}
.pie:before {
inset:0;
background:
radial-gradient(farthest-side,var(--c) 98%,#0000) top/var(--b) var(--b) no-repeat,
conic-gradient(var(--c) calc(var(--p)*1%),#0000 0);
-webkit-mask:radial-gradient(farthest-side,#0000 calc(99% - var(--b)),#000 calc(100% - var(--b)));
        mask:radial-gradient(farthest-side,#0000 calc(99% - var(--b)),#000 calc(100% - var(--b)));
}
.pie:after {
inset:calc(50% - var(--b)/2);
background:var(--c);
transform:rotate(calc(var(--p)*3.6deg)) translateY(calc(50% - var(--w)/2));
}
.animate {
animation:p 1s .5s both;
}
.piepass{
    --c:#97bd61;
}
.piefail{
    --c:#ce3e01;
}
.pieskip{
    --c:#fed84f;
}
.section{
    float: left;
    padding: 1%;
}
.dt_time{
    padding-top: 5em;
    padding-right: 1em;
    text-align: right;
    color: black;
    font-weight: bold;
    font-family: 'Courier New', Courier, monospace;
}
.section { margin-bottom: 1em; color: black; cursor: pointer; font-family: 'Courier New', Courier, monospace; font-size: small; font-weight: bold;}

.printer{
    /* position: absolute; */
    padding-right: 1em;
    float: right;
    color: black;
    font-weight: bold;
    font-family: 'Courier New', Courier, monospace;
}
@media print {
  #printPageButton {
    display: none;
  }
}

"""

@library(scope="GLOBAL")
class SummaryReport:
    
    ROBOT_LISTENER_API_VERSION = 1
    
    def __init__(self) -> None:

        self.title_doc = "No docu found"
        self.title_disc = 'Lorem ipsum ...'
        self.test_cases = []
        self.test_cases_status = []
        self.test_cases_start = []
        self.test_cases_ended = []
        self.homdir = os.path.expanduser("~")
        self.user_profile = self.homdir + "\\"
        self.open_user_profile = os.path.realpath(self.user_profile)


    def parse_xml_html(self,xml_path):
        now = datetime.now()
        self.dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        # test case name
        for x in root.findall(".//suite/test"):
            self.test_cases.append(x.attrib["name"])
        # test case status
        for x in root.findall(".//test/status"):
            self.test_cases_status.append(x.attrib["status"])
        # test case starttime
        for x in root.findall(".//test/status"):
            self.test_cases_start.append(x.attrib["starttime"][8:])
        # test case endtime
        for x in root.findall(".//test/status"):
            self.test_cases_ended.append(x.attrib["endtime"][8:])

        self.All_tests_count = len(self.test_cases)
        self.Passes = self.test_cases_status.count("PASS")
        self.Failes = self.test_cases_status.count("FAIL")
        self.Skipes = self.test_cases_status.count("SKIP")
        
        self.Passes_pec = round((self.Passes / self.All_tests_count)*100,2)
        self.Failes_pec = round((self.Failes / self.All_tests_count)*100,2)
        self.Skipes_pec = round((self.Skipes / self.All_tests_count)*100,2)
        self.generate_html()
        

    def generate_html(self):
        doc = dominate.document(title="Repo-Reporting")
        
        with doc.head:
            link(rel='stylesheet', href='style.css')
           
        with doc:
            style(css)
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
                with table().add(tbody()):
                    with tr():
                        th("Test Case")
                        th("Status")
                        th("Started")
                        th("Ended")
                    for x,y,s,e in zip (self.test_cases,self.test_cases_status,self.test_cases_start,self.test_cases_ended):
                        tr()
                        td(x)
                        if y == "PASS":
                            td(span(y,cls="label Pass"))
                        if y == "SKIP":
                            td(span(y,cls="label Skip"))
                        if y == "FAIL":
                            td(samp(y,cls="label Fail"))
                        td(s)
                        td(e)
                div(self.dt_string,cls="dt_time")
        
        os.startfile(self.open_user_profile)
        
        with open(f"{self.user_profile}Sammary.html","w+") as file:
            file.write(doc.render())

        with open(f"{self.user_profile}style.css","w+") as file:
            file.write(css)
        
    
if __name__ == "__main__":
    original_output_xml = sys.argv[1]
    if not os.path.isfile(original_output_xml):
        raise FileNotFoundError(f'{original_output_xml} is not a valie xml path')
    sr = SummaryReport()
    sr.parse_xml_html(original_output_xml)
