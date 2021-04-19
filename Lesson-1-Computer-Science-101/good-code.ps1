# Commands
# Readable
# Good use of white spaces


# Write an output of hello world
Write-Output = 'Hello World'

Write-Host = 'Testing'

# Function that writes 'Hello' and 'Hello World'
function testing {
    Write-Host 'Hello'

    # Variable that contains the 'World' value
    $test1 = 'World'
    Write-Host = "Hello $test1"
}