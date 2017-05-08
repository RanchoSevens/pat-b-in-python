n = input()

for i in range(n):

    a, b, c = map( int, raw_input().split() )

    print "Case #%d:" % ( i + 1 ),

    if a + b > c:

        print "true"
    else:
    
        print "false"
