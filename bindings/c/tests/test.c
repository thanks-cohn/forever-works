#include "forever.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void){fw_error e={{0},{0}};fw_model*m=fw_load("conformance/fixtures/complete/forever",&e);char*s;if(!m){fprintf(stderr,"%s\n",e.message);return 1;}if(!fw_validate(m,&e)||fw_record_count(m)<10||!fw_get_entity_json(m,"dependency.old-streamer")){fprintf(stderr,"validation/query failed: %s\n",e.message);return 2;}s=fw_serialize(m);if(!s||!strstr(s,"intent.remote-transfer")){fprintf(stderr,"serialization failed\n");return 3;}free(s);fw_free(m);puts("C binding conformance smoke passed");return 0;}
