#include "headers.h"
using namespace std;

Person::Person(string name, string lastname, int age)
{
    : name(name),lastname(lastname), age(age)
    // this->name = name;
    // this->lastname = lastname;
    // this->age = age;
};
Person::~Person()
{
};
void Person::SOutputIdentity()
{
};

// void Person::OutputAge()
// {
//   cout << "I am" << this->age << "X years old" << endl;
// };
