'''Created by Angela Huang
18:59 Dec 17
'''

import client
import os
from jenkinsapi.jenkins import Jenkins


class JenkinsJobCrawler():

    buildno = 0
    lastnbuilds = []

    def find_between(self, s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""

    def get_server_instance(self):
        jenkins_url = 'http://ci.dev.beetalk.com'
        username = "huangaq@garena.com"
        apiToken = "662f2765b0feb6b432b532ef17127fae"
        server = Jenkins(jenkins_url, username, apiToken)
        return server

    def broadcast_chat(self, uids, text):
        client.discussion_send_chat(
                usr='6500007816', pwd=None, text=text, title='Jenkins',
                uids=uids)
#         client.btalk_send_chat(
#             from_phone='6500007816', pwd=None, to_id=15808182,
#             text=text, chat_type=0, whisperDuration=10)

    def get_job_details(self, jobname):
        # Refer Example #1 for definition of function 'get_server_instance'

        server = self.get_server_instance()
        lastbuild = server[jobname].get_last_build()
        build_before_last_build = server[jobname].get_build(lastbuild.buildno-1)
        changes = ''

        if lastbuild.buildno != self.buildno:
            if lastbuild.get_status() != 'SUCCESS':
                text = 'Damn! Last build of beetalk-2.3-install #%s is %s.\n' \
                     % (lastbuild.buildno, lastbuild.get_status())
                self.broadcast_chat(uids=[15808182,22907791,2195697,110276], text=text)
            if lastbuild.get_status() == 'SUCCESS' and build_before_last_build.get_status() == 'FAILURE':
                text = 'Last build of beetalk-2.3-install #%s is back to normal. Good Job!\n' \
                     % (lastbuild.buildno)
                self.broadcast_chat(uids=[15808182,22907791,2195697,110276], text=text)
            self.buildno = lastbuild.buildno

if __name__ == '__main__':

    J = JenkinsJobCrawler()
    jobname = 'beetalk-2.3-install'
    if 'JENKINS_JOB' in os.environ:
        jobname = os.environ['JENKINS_JOB']
    J.get_job_details(jobname)
#     J.run_script_summary()

# end of file

