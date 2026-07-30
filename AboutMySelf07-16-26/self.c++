#include <iostream>
using namespace std;

void printHeader();
void displayProfile(string pet, string name, string nickname,
                    string birthday, string address,
                    string favSong, string motivation,
                    string support);
void printFooter();

int main() {

    // My Information
    string pet = "Dog";
    string name = "Tharen Honrade";
    string nickname = "Thata";
    string birthday = "01/10/2006";
    string address = "Taban-Manguining, Alimodian";
    string favSong = "Feel Good Inc. - Gorillaz";
    string motivation = "To become the best version of myself and make myself happy.";
    string support = "Financial support and someone to celebrate my small wins in life.";

    printHeader();

    displayProfile(
        pet,
        name,
        nickname,
        birthday,
        address,
        favSong,
        motivation,
        support
    );

    printFooter();

    return 0;
}

void printHeader() {

    cout << "=============================================================\n";
    cout << "                 🌿 GET TO KNOW ME 🌿\n";
    cout << "=============================================================\n";
    cout << "                A little glimpse about myself\n\n";
}

void displayProfile(string pet, string name, string nickname,
                    string birthday, string address,
                    string favSong, string motivation,
                    string support) {

    if (pet == "Dog" || pet == "dog")
        cout << "🐶 🐶 🐶 DOG PERSON 🐶 🐶 🐶\n";
    else
        cout << "🐱 🐱 🐱 CAT PERSON 🐱 🐱 🐱\n";

    cout << "\n📌 PROFILE INFORMATION\n";
    cout << "-------------------------------------------------------------\n";

    cout << "👤 Name        : " << name << " (" << nickname << ")" << endl;
    cout << "🎂 Birthday    : " << birthday << endl;
    cout << "🏡 Home Base   : " << address << endl;
    cout << "🎵 On Repeat   : " << favSong << endl;
    cout << "💪 Motivation  : " << motivation << endl;
    cout << "🤝 Support     : " << support << endl;
}

void printFooter() {

    cout << "\n=============================================================\n";
    cout << "           ✨ THANK YOU FOR GETTING TO KNOW ME! ✨\n";
    cout << "=============================================================\n";