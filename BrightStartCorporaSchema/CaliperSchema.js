//Audio File
const audioSchema = {
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id": "{url}/audio/{id}",
    "name": "{file_name}",
    "type": "MediaObject",
    "datePublished": "{date}",
    "duration": "{duration}", // in seconds
    "part":
    [{
        "id": "{url}/audio/{id}/{segment_id}",
        "type": "MediaObject",
        "name": "{segment_name}",
        "startedAtTime": "{start_time}",
        "endedAtTime": "{end_time}",
        "isPartOf": 
        {
            "id": "{url}/audio/{id}",
            "type": "MediaObject",
            "name": "{file_name}"
        }
    }],
    "extensions": {
        "pitch": "{pitch}" //possible for gender recogntion
    }
}

//Transcription Schema
const transcriptionSchema = {
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id": "{url}/transcription/{id}",
    "type": "AnnotationEvent",
    "profile": "AnnotationProfile",
    "name": "Transcription",
    "actor":                            //Reader Information
    {
        "id": "{url}/reader/{id}",
        "type": "Person",
        "name": "Jane Doe"
    },
    "action": "Annotated",
    "object": 
    {
        "id": "{url}/text/{transcription_text_id}", //Text File
        "type": "Text",
        "value": "{\"text\": \"This is a transcription\"}",
        "name": "Transcription Text"
    },
    "session":
    {
        "id": "{url}/sessions/{session_id}",
        "type": "Session",
        "startedAtTime": "{start_time}",
        "endedAtTime": "{end_time}"
    }

}

//Transcription Analysis Schema
const transcriptionAnalysisSchema = {
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id": "{url}/transcription_analysis/{id}",
    "type": "AnnotationEvent",
    "actor":
    {
        "id": "{url}/reader/{id}",
        "type": "Person"
    },
    "action": "Annotated",
    "isPartOf":
    {
        "id": "{url}/transcription/{transcription_id}", //FK to transcription
        "type": "AnnotationEvent",
        "name": "Transcription"
    },
    "object":
    {
        "id": "{url}/transcription_errors/{id}", //FK to Error Schema
        "type": "Annotation",
        "name": "Transcription Analysis"
    }
    
}