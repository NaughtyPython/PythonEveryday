'''Created by Angela Huang
18:59 Dec 17
'''
import json
import requests
import logging
import jenkins.crawler
from jenkins.crawler import JenkinsJobCrawler

logger = logging.getLogger(__name__)


def init_logger(debug=False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format='[%(filename)s: %(lineno)s] %(message)s')


class MyCrawler(JenkinsJobCrawler):
    def crawling(self, jobname, obj):
        buildNumber = self.get_number(obj)
        result = self.get_result(obj)

        if buildNumber != self.buildno:
            if result == 'FAILURE':
                changelog = self.get_brief_changelog(obj, True)
                text = 'Damn! Last build of %s #%s is %s.\nChangelog:\n%s' \
                    % (jobname, buildNumber, result, changelog)
            else:
                changelog = self.get_brief_changelog(obj, False)
                text = 'Last build of %s #%s is %s.\nChangelog:\n%s' \
                    % (jobname, buildNumber, result, changelog)

            self.broadcast_chat(uids=[15808182, 22907791, 2195697, 110276],
                                text=text)
            self.buildno = buildNumber


if __name__ == '__main__':
    init_logger(debug=True)
    J = MyCrawler()
    jobname = 'beetalk-android'
    r = requests.get(
        'http://%s/job/%s/lastBuild/api/json' %
        (jenkins.crawler.JENKINS_DOMAIN, jobname),
        auth=('%s' % jenkins.crawler.USER, "%s" % jenkins.crawler.TOKEN))

#     For debug:

#     jobname = 'iOS-BeeTalk'
#     r = requests.get(
#         "http://%s/job/%s/44/api/json" %
#         (JENKINS_DOMAIN, jobname),
#         auth=('%s' % USER, "%s" % TOKEN))

    obj = json.loads(r.text)
    J.crawling(jobname, obj)


# end of file
