#include <pybind11/pybind11.h>
#include <string>
namespace py = pybind11;

std::string concat(const std::string &a, const std::string &b) {
    return a + b;
}

PYBIND11_MODULE(cppconcat, m) {
    m.def("concat", &concat, "Concatenate two strings");
}
