@echo off
cls
for /l %%N in (1 1 30) do (
    echo running client.py
    python client.py
    echo %%N
)
pause