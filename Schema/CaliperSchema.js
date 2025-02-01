//Audio File
{
    "@context"; "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id"; String,
    "name"; String,
    "type"; "MediaObject",
    "datePublished"; String,
    "duration"; Number // in seconds
    "extensions";{
        "pitch"; Number //possible for gender recogntion
    }

    "part";[{
        "id": String,
        "type": "MediaObject",
        "name": String,
        "startedAtTime": "{start_time}",
        "endedAtTime": "{end_time}",
        "isPartOf": {
            "id": String,
            "type": "MediaObject",
            "name": String
        }

    }]
}

//Transcription Schema
{
    "@context"; "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id"; "http://example.edu/events/1234",
    "type"; "AnnotationEvent",
    "profile"; "AnnotationProfile",
    "actor"; {
        "id"; "http://example.edu/user/554433",
        "type"; "Person",
        "name"; "Jane Doe"
    }
    "action"; "Annotated",
    "object"; {
        "id"; "http://example.edu/objects/1234",
        "type"; "Text",
        "value";"{\"text\": \"This is a transcription\"}"
        "name"; "Transcription"
    }
    "session";{
        "id"; "http://example.edu/sessions/1234",
        "type"; "Session",
        "startedAtTime"; "{start_time}",
        "endedAtTime"; "{end_time}"
    }

}

//Transcription Analysis Schema
{
    "@context"; "http://purl.imsglobal.org/ctx/caliper/v1p2",
    "id"; "http://example.edu/events/1234",
    "transcription_id"; String, //FK to transcription
    "type"; "AnnotationEvent",
    "actor";{
        "id"; String,
        "type"; "Person"
    }
    "action"; "Annotated",
    "object"; {
        "id"; String,
        "type"; "Annotation"
        "name"; "Transcription Analysis",
        "extensions"; {
            "mispronunciations"; [{
                "expected_word": String, 
                "actual_word": String
            }],
            "repetitions"; [{
                "word": String,
                "count": Number
            }],
            "unfinished_words"; [{
                "word": String
            }],
            "pauses"; [{ 
                "word": String,
                "count": Number,
            }],
            
            "long_pauses"; [{
                "word": String,
                "count": Number
            }],
            "non_speech_sounds"; Number
        }
    }
    
}