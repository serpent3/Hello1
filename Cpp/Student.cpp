#include "headers.h"
using namespace std;

Student::Student(string name, string lastname)
{
    this->name = name;
    this->lastname = lastname;
};
Student::~Student()
{
};
void Student::SitInClass()
{
    cout << this->name << " sitting in main theater" << endl;
};
