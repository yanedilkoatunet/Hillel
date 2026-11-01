import logging
from datetime import datetime, timedelta


KEY = "TSTFEED0300|7E3E|0400"


def read_filtered_log(filename):
    filtered_log = []

    with open(filename, "r") as file:
        for line in file:
            if KEY in line:
                filtered_log.append(line.strip())

    return filtered_log


def get_timestamp(line):
    timestamp_index = line.find("Timestamp ")

    if timestamp_index == -1:
        return None

    timestamp = line[timestamp_index + 10:timestamp_index + 18]

    return datetime.strptime(timestamp, "%H:%M:%S")


def analyze_heartbeat(filename):
    logging.basicConfig(
        filename="hb_test.log",
        filemode="w",
        level=logging.WARNING,
        format="%(levelname)s | %(message)s"
    )

    logger = logging.getLogger(__name__)

    filtered_log = read_filtered_log(filename)

    timestamps = []

    for line in filtered_log:
        timestamp = get_timestamp(line)

        if timestamp is not None:
            timestamps.append(timestamp)

    for i in range(len(timestamps) - 1):
        current_time = timestamps[i]
        next_time = timestamps[i + 1]

        difference = current_time - next_time

        if difference.total_seconds() < 0:
            difference += timedelta(days=1)

        seconds = difference.total_seconds()

        if 31 < seconds < 33:
            logger.warning(
                "Heartbeat issue at %s. Difference: %s seconds",
                current_time.strftime("%H:%M:%S"),
                seconds
            )

        elif seconds >= 33:
            logger.error(
                "Heartbeat issue at %s. Difference: %s seconds",
                current_time.strftime("%H:%M:%S"),
                seconds
            )


analyze_heartbeat("hblog.txt")
