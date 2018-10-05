#include "headers.h"
using namespace std;

class Student
{
private:
    string name;
    string lastname;
public:
    Student(string name, string lastname);
    ~Student();
    void SitInClass();
};
