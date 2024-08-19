// gcc -g -I ../includes -o integers integers.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>

// Hidden for simplicity
#include "wargames.h"
#include "integers.h"

void demo_unsigned()
{
    print_unsigned_banner();

    // Define an unsigned integer
    unsigned int bar = 44;
    printf("bar is %u\n", bar);

    // Example #2
    bar = 10000000;
    printf("bar is %u in base-10 (decimal)\n", bar);
    printf("bar is 0x%08X in base-16 (hex)\n", bar);

    // Example #3
    bar = 0x81818181;
    printf("bar is %u in base-10 (decimal)\n", bar);
    printf("bar is 0x%08X in base-16 (hex)\n", bar);

    // User quiz
    quiz_unsigned();
}

void demo_signed()
{
    print_signed_banner();

    // Define a signed integer
    int foo = -44;
    printf("foo is %d\n", foo);

    // Example #2
    foo = 10000000;
    printf("foo is %d in base-10 (decimal)\n", foo);
    printf("foo is 0x%08X in base-16 (hex)\n", foo);

    // Example #3
    foo = 0x81818181;
    printf("foo is %d in base-10 (decimal)\n", foo);
    printf("foo is 0x%08X in base-16 (hex)\n", foo);

    // User quiz
    quiz_signed();
}

void demo_limits()
{
    print_limits_banner();

    //
    // Unsigned Integers
    //

    uint8_t u8 = 10;
    printf("\nu8 is %u, its value can span from %u to %u\n", u8, 0, UINT8_MAX);

    uint16_t u16 = 1000;
    printf("u16 is %u, its value can span from %u to %u\n", u16, 0, UINT16_MAX);

    uint32_t u32 = 123456789;
    printf("u32 is %u, its value can span from %u to %u\n", u32, 0, UINT32_MAX);

    uint64_t u64 = 9999999999999999;
    printf("u64 is %" PRIu64 ", its value can span from %u to %" PRIu64 "\n", u64, 0, UINT64_MAX);
    press_enter();

    //
    // Signed Integers
    //

    int8_t s8 = 10;
    printf("s8 is %d, its value can span from %d to %d\n", s8, INT8_MIN, INT8_MAX);

    int16_t s16 = -1000;
    printf("s16 is %d, its value can span from %d to %d\n", s16, INT16_MIN, INT16_MAX);

    int32_t s32 = 123456789;
    printf("s32 is %d, its value can span from %d to %d\n", s32, INT32_MIN, INT32_MAX);

    int64_t s64 = -5153692927956318;
    printf("s64 is %" PRId64 ", its value can span from %" PRId64 " to %" PRId64 "\n", s64, INT64_MIN, INT64_MAX);

    // user quiz
    quiz_limits();
}

void demo_overflows()
{
    print_overflows_banner();

    //
    // Unsigned Integers
    //

    puts("Overflowing 32bit unsigned integer...");

    uint32_t u32 = UINT32_MAX - 2;
    for (int i = 0; i < 6; i++)
    {
        printf("u32 is %u (0x%08X), incrementing...\n", u32, u32);
        u32++;
    }
    press_enter();

    puts("\nUnderflowing 32bit unsigned integer...");
    for (int i = 0; i < 6; i++)
    {
        printf("u32 is %u (0x%08X), decrementing...\n", u32, u32);
        u32--;
    }
    press_enter();

    //
    // Signed Integers
    //

    puts("\nOverflowing 32bit signed integer...");

    int32_t s32 = INT32_MAX - 2;
    for (int i = 0; i < 6; i++)
    {
        printf("s32 is %d (0x%08X), incrementing...\n", s32, s32);
        s32++;
    }
    press_enter();

    puts("\nUnderflowing 32bit signed integer...");
    for (int i = 0; i < 6; i++)
    {
        printf("s32 is %d (0x%08X), decrementing...\n", s32, s32);
        s32--;
    }

    // user quiz
    quiz_overflows();
}

void print_menu()
{
    printf("-- Integer Playground ---------------\n"
           " 1. Unsigned Integers Quiz           \n"
           " 2. Signed Integers Quiz             \n"
           " 3. Integer Limits Quiz              \n"
           " 4. Integer Overflows Quiz           \n"
           " 5. Quit                             \n"
           "-------------------------------------\n"
           "Enter Choice: ");
}

void main()
{
    init_wargame();

    printf("------------------------------------------------------------\n");
    printf("--[ C Fundamentals - Integers                               \n");
    printf("------------------------------------------------------------\n");

    unsigned int choice = 0;

    while (1)
    {
        print_menu();
        if ((choice = get_number()) == EOF)
            break;

        if (choice == 1)
            demo_unsigned();
        else if (choice == 2)
            demo_signed();
        else if (choice == 3)
            demo_limits();
        else if (choice == 4)
            demo_overflows();
        else if (choice == 5)
            break;
        else
            puts("Invalid choice!");

        choice = 0;
    }
}
