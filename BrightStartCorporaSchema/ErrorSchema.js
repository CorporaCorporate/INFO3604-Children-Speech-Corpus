
//Error Schema
const errorSchema = {
    "id": "{url}/transcription_errors/{id}",
    "mispronunciations": [{
        "expected_word": "{word}", 
        "actual_word": "{actual_word}"
    }],
    "repetitions": [{
        "word": "{word}",
        "count": "{count}"
    }],
    "unfinished_words": [{
        "word": "{word}",
        "count": "{count}"
    }],
    "pauses": [{ 
        "word": "{word}",
        "count": "{count}",
    }],
    
    "long_pauses": [{
        "word": "{word}",
        "count": "{count}"
    }],
    "non_speech_sounds": "{count}"
}