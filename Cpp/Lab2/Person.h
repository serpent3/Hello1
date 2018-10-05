#include "headers.h"
using namespace std;

class Person
{
private:
    string name;
    string lastname;
    int age;
protected:
    string phone;
public:
    Person(string name, string lastname, int age);
    virtual ~Person();
    void SitInClass();
    virtual void SOutputIdentity();
    // virtual void OutputAge();
};
