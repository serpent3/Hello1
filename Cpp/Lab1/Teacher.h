#include "headers.h"
using namespace std;

class Teacher
{
private:
    string name;
    string lastname;
public:
    Teacher(string name, string lastname);
    ~Teacher();
    void GradeStudent();
    void SitInClass();
};
