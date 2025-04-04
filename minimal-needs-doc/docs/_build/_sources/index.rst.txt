Piano Practice Recoder
=============

.. req:: Detect Piano Start
    :id: REQ001

    The system shall detect when the electronic piano is turned on.

.. req:: Detect Piano Stop
    :id: REQ002

    The system shall detect when the electronic piano is turned off.

.. req:: Record Audio
    :id: REQ003

    The system shall record audio during the practice session.

.. req:: Store Audio on Storage
    :id: REQ004

    The system shall store the recorded audio either in Google Drive or NAS or Cloud.

.. req:: Remove Silence
    :id: REQ005

    The system shall remove silent periods longer than a specified threshold from the recording.

.. req:: Log Practice Time
    :id: REQ006

    The system shall log the session start time, stop time, and total duration.

.. req:: Send Email Notification
    :id: REQ007

    The system shall send an email with session information, including start time, stop time, total duration, and a link to the processed audio.

.. req:: Web Portal for History
    :id: REQ008

    The system shall provide a website that displays daily practice logs and allows playback of past recordings.

.. req:: Real-time Streaming (Optional)
    :id: REQ009

    The system may support real-time streaming of the piano session.

.. req:: Silence Threshold
    :id: CST001

    Silence is defined as a continuous period of no audio for more than a configurable number of seconds (e.g., 5 seconds).

.. req:: Detect Piano Power On
    :id: FUNC001

    Detects when the piano is powered on.

.. req:: Detect Piano Power Off
    :id: FUNC002

    Detects when the piano is powered off.

.. req:: Start Audio Recording
    :id: FUNC003

    Starts audio recording once the piano is turned on.

.. req:: Save Audio File
    :id: FUNC004

    Saves the recorded audio to a predefined storage.

.. req:: Process and Trim Silence
    :id: FUNC005

    Removes silent sections based on the silence threshold.

.. req:: Log Session Data
    :id: FUNC006

    Logs session metadata: start time, end time, duration.

.. req:: Send Summary Email
    :id: FUNC007

    Sends an email containing session information and the recording link.

.. req:: Display Log via Web
    :id: FUNC008

    Provides a web interface for reviewing daily logs and playback.

.. req:: Stream Audio in Real-time
    :id: FUNC009

    Streams audio live during the session.
