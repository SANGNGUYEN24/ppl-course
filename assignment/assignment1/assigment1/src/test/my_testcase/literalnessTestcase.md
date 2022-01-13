# Testing number
```
init:   INTEGER_LITERALNESS 
        |FLOAT_LITERALNESS
        |OCTAL_LITERALNESS
        |HEXA_LITERALNESS
        |BINARY_LITERALNESS
        |BOOST_LITERALNESS
```
## INTEGER
**Sucess**

- 2 tokens


    0 1 2 3 4 5 6 7 8 9     
    -0 -1 -2 -3 -4 -5 -6 -7 -8 -9   
    +0 +1 +2 +3 +4 +5 +6 +7 +8 +9   
    -1001212    
    +101232     
    123     
    1234_12_13  
    -100_000_000    
    +200_000


- 3 tokens


    -0834

**Fail**

    _1223   
    08 09 -> OCTAL

## FLOAT
**Success** 
- 2 tokens 


    +or-10.10   
    +or-10.20e10  
    +or-10.20e-10

    +or-10.e10    
    +or-10.

    +or-.0    
    +or-.10   
    +or-.10e10   

    +or-1_23.123e10     
    +or-1_23.123_123e10   
    +or-10_000.20_225e10_000
    +or-10_000.20_225e1_000

- 3 tokens


    +-1_23.123e10     
    +-1_23.123_123e10   
    +-10_000.20_225e10_000
    +-10_000.20_225e1_000
    -+1_23.123e10 
    -+1_23.123_123e10   
    -+10_000.20_225e10_000
    -+10_000.20_225e1_000

    +-10_000.020_225e1_000
    +-010_000.020_225e01_000

    2E-10

**Fail**

    '.'     
    e10 
    .e10














