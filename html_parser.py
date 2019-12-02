from bs4 import BeautifulSoup
import sys
import re
cmdargs = str(sys.argv)

# with open(sys.argv[1]), 'r') as myfile:
#     data=myfile.read().replace('\n', '')
file = open(sys.argv[1], 'r')

soup = BeautifulSoup(file, 'html.parser')

email = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblEmailId_*')})
name = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblName_*')})
designation = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_rpIASDesignation_lblIASDesignation_*')})
officename = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_rpIASOffice_lblIASOfficeName_*')})
officeaddress = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblOfficeAddress_*')})
officenumber = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_rpIASOfficeNumber_lblIASOfficeNumber_*')})

residencenumber = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblResidencePhoneNumber_*')})
mobilenumber = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblMobileNumber_*')})
faxnumber = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_rptFaxNumber_lblIASFaxNumber_*')})
recruitmentmode = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblRecruitmentMode_*')})
batchyear = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblBatchyear_*')})
nativeplace = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblNativePlace_*')})
dob = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblDOB_*')})
dateofappointment = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblDateofAppointmenttoIAS_*')})
dateofpresentpost = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblDateofAppointmenttoPresentpost_*')})
pay = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblPayandSpecialPay_*')})
qualification = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblEducationalQualification_*')})
remarks = soup.findAll("span", {"id" : re.compile('ContentPlaceHolder1_UserDisplayIAS1_rptIASMain_gvIAS_lblRemarks_*')})

# print "Printing names:\n"
# print len(names)
# print "\n";

# print "Printing courses:\n"
# print len(courses)
# print "\n";

# print "Printing collages:\n"
# print len(collages)
# print "\n";

# print "Printing emails:\n"
print len(remarks)

# print "\n";
for x in xrange(0,len(email)):
	print email[x].string,'|',name[x].string,'|',designation[x].string,'|',officename[x].string,'|',officeaddress[x].string,'|',officenumber[x].string,'|',residencenumber[x].string,'|',mobilenumber[x].string,'|',faxnumber[x].string,'|',recruitmentmode[x].string,'|',batchyear[x].string,'|',nativeplace[x].string,'|',dob[x].string,'|',dateofappointment[x].string,'|',dateofpresentpost[x].string,'|',pay[x].string,'|',qualification[x].string,'|',remarks[x].string