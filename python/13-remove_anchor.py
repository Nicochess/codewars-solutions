def remove_url_anchor(url):
    anchor_index = url.find('#')
    return url[:anchor_index] if anchor_index > 0 else url