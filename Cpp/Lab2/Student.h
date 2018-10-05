#include "headers.h"
using namespace std;

class Student : public Person
{
private:
    string name;
    string lastname;
public:
    Student(string name, string lastname, int age);
    virtual ~Student();
    // void SitInClass();
    virtual void SOutputIdentity();
};
