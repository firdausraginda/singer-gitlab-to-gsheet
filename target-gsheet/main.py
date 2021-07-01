import sys
import io
import json
import singer
from jsonschema.validators import Draft4Validator
from src.gsheet_access import write_to_spreadsheet

logger = singer.get_logger()

def persist_json_outputs(json_outputs):
    schemas = {}
    key_properties = {}
    validators = {}
    
    # Loop over json_outputs from stdin
    for json_output in json_outputs:

        # try to read the json output
        try:
            json_output = json.loads(json_output)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(json_output))
            raise
        
        # check type key
        if 'type' not in json_output:
            raise Exception("json_output is missing required key 'type': {}".format(json_output))
        
        type_output = json_output['type']

        if type_output == 'RECORD':

            # check stream key
            if 'stream' not in json_output:
                raise Exception("json_output is missing required key 'stream': {}".format(json_output))
            
            # check stream name
            if json_output['stream'] not in schemas:
                raise Exception("A record for stream {} was encountered before a corresponding schema".format(o['stream']))

            # get schema for this record's stream
            # schema = schemas[json_output['stream']]

            # Validate record
            validators[json_output['stream']].validate(json_output['record'])

            write_to_spreadsheet(json_output['record'])

        elif type_output == 'SCHEMA':

            # check stream key
            if 'stream' not in json_output:
                raise Exception("json_output is missing required key 'stream': {}".format(json_output))

            stream = json_output['stream']
            schemas[stream] = json_output['schema']
            validators[stream] = Draft4Validator(json_output['schema'])

            # check key_properties key
            if 'key_properties' not in json_output:
                raise Exception("key_properties field is required")

            key_properties[stream] = json_output['key_properties']
        else:
            raise Exception("Unknown message type {} in message {}".format(json_output['type'], json_output))
    
    return json_output

def main():
    result = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    persist_json_outputs(result)

if __name__ == '__main__':
    main()