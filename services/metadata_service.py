import re

def extract_metadata(item):

    text = (
        item.get("title","") + " " +
        item.get("description","")
    ).lower()

    metadata = {}

    # modality

    if "video" in text:
        metadata["modality"] = "Video"

    elif "image" in text or "face" in text:
        metadata["modality"] = "Image"

    elif "audio" in text or "voice" in text:
        metadata["modality"] = "Audio"

    else:
        metadata["modality"] = "Unknown"

    # task

    if "detection" in text:
        metadata["task"] = "Detection"

    elif "classification" in text:
        metadata["task"] = "Classification"

    elif "segmentation" in text:
        metadata["task"] = "Segmentation"

    else:
        metadata["task"] = "Unknown"

    # dataset size

    m = re.search(r'([\d,]+)\s*(images|videos|samples)', text)

    if m:
        metadata["dataset_size"] = m.group(0)
    else:
        metadata["dataset_size"] = "Unknown"

    return metadata