#include "forever.hpp"
#include <iostream>
int main(){foreverworks::model m("conformance/fixtures/complete/forever");m.validate();if(m.size()<10||m.entity("dependency.old-streamer").empty()||m.serialize().empty())return 1;std::cout<<"C++ wrapper conformance smoke passed\n";}
