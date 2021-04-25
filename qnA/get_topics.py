import RAKE


def get_topics(text):
    stop_lists = (
        RAKE.SmartStopList()
        + RAKE.FoxStopList()
        + RAKE.NLTKStopList()
        + RAKE.MySQLStopList()
        + RAKE.GoogleSearchStopList()
    )
    Rake = RAKE.Rake(stop_lists)
    topics = []
    for x, _ in Rake.run(text)[:2]:
        words = x.split()
        topics.extend(words)
    return topics
