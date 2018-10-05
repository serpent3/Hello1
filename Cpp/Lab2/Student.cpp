#include "headers.h"
using namespace std;

Student::Student(string name, string lastname, int age)
{
  : Person(name, lastname, age)
    // this->name = name;
    // this->lastname = lastname;
    // this->age = age;
};
Student::~Student()
{
};
// void Student::SitInClass()
// {
//     cout << this->name << " sitting in main theater" << endl;
// };
void Student::SOutputIdentity()
{
  Person::SOutputIdentity();
  cout << this->name << " sitting in main theater" << endl;
};
