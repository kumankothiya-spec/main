import pytest
from pymodbus.client import ModbusTcpClient

@pytest.mark.smoke
def test_holding_reg_read():
    client = ModbusTcpClient("127.0.0.1", port=5020)
    client.connect()
    rr = client.read_holding_registers(0, 2)
    client.close()
    assert [20,30] == rr.registers
