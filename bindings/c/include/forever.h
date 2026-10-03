#ifndef FOREVER_H
#define FOREVER_H
#include <stddef.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct fw_model fw_model;
typedef struct { char code[40]; char message[256]; } fw_error;
fw_model *fw_load(const char *model_directory, fw_error *error);
void fw_free(fw_model *model);
size_t fw_record_count(const fw_model *model);
const char *fw_get_entity_json(const fw_model *model, const char *id);
int fw_validate(const fw_model *model, fw_error *error);
char *fw_serialize(const fw_model *model); /* caller frees with free() */
#ifdef __cplusplus
}
#endif
#endif
