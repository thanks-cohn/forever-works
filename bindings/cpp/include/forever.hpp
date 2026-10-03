#ifndef FOREVER_HPP
#define FOREVER_HPP
#include "forever.h"
#include <cstdlib>
#include <stdexcept>
#include <string>
namespace foreverworks {
class model {
 fw_model *value_{};
public:
 explicit model(const std::string& path){fw_error e{};value_=fw_load(path.c_str(),&e);if(!value_)throw std::runtime_error(e.message);}
 ~model(){fw_free(value_);} model(const model&)=delete; model& operator=(const model&)=delete;
 model(model&&o) noexcept:value_(o.value_){o.value_=nullptr;}
 std::size_t size()const noexcept{return fw_record_count(value_);}
 std::string entity(const std::string&id)const{auto p=fw_get_entity_json(value_,id.c_str());if(!p)throw std::out_of_range(id);return p;}
 void validate()const{fw_error e{};if(!fw_validate(value_,&e))throw std::runtime_error(e.message);}
 std::string serialize()const{char*p=fw_serialize(value_);if(!p)throw std::bad_alloc();std::string s(p);std::free(p);return s;}
};
}
#endif
