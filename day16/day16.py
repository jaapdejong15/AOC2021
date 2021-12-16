from functools import reduce

from helper import parsing

def part1(hex_data):
    def read_packet(start_position):
        version = int(binary_data[start_position:start_position+3], 2)
        typeID = int(binary_data[start_position+3:start_position+6], 2)
        pos = start_position + 6
        if typeID == 4:
            binary_representation = ''
            while binary_data[pos] == '1':
                binary_representation += binary_data[pos+1:pos+5]
                pos += 5
            binary_representation += binary_data[pos+1:pos+5]
            pos += 5
            return pos, version
        else:
            length_type_id = binary_data[pos]
            pos += 1
            total_length = float('inf')
            total_number_of_packets = float('inf')
            if length_type_id == '0':
                total_length = pos + 15 + int(binary_data[pos:pos+15], 2)
                pos += 15
            elif length_type_id == '1':
                total_number_of_packets = int(binary_data[pos:pos+11], 2)
                pos += 11
            num_packets = 0
            s = version
            while pos < total_length and num_packets < total_number_of_packets:
                pos, id_sum = read_packet(pos)
                s += id_sum
                num_packets += 1
            return pos, s

    binary_data = ''
    for char in hex_data:
        n = int(char, 16)
        binary_data += format(n, 'b').zfill(4)
    _, answer = read_packet(0)
    print(f'Answer for part 1: {answer}')

def part2(hex_data):
    def read_packet(start_position):
        typeID = int(binary_data[start_position+3:start_position+6], 2)
        pos = start_position + 6
        if typeID == 4:
            binary_representation = ''
            while binary_data[pos] == '1':
                binary_representation += binary_data[pos+1:pos+5]
                pos += 5
            binary_representation += binary_data[pos+1:pos+5]
            pos += 5
            number = int(binary_representation, 2)
            return pos, number
        else:
            length_type_id = binary_data[pos]
            pos += 1
            total_length = float('inf')
            total_number_of_packets = float('inf')
            if length_type_id == '0':
                total_length = pos + 15 + int(binary_data[pos:pos+15], 2)
                pos += 15
            elif length_type_id == '1':
                total_number_of_packets = int(binary_data[pos:pos+11], 2)
                pos += 11
            num_packets = 0
            packet_values = []
            while pos < total_length and num_packets < total_number_of_packets:
                pos, packet_value = read_packet(pos)
                packet_values.append(packet_value)
                num_packets += 1

            if typeID == 0:
                return pos, sum(packet_values)
            elif typeID == 1:
                packet_values.append(1)
                return pos, reduce(lambda x, y : x * y, packet_values)
            elif typeID == 2:
                return pos, min(packet_values)
            elif typeID == 3:
                return pos, max(packet_values)
            elif typeID == 5:
                return pos, 1 if packet_values[0] > packet_values[1] else 0
            elif typeID == 6:
                return pos, 1 if packet_values[0] < packet_values[1] else 0
            elif typeID == 7:
                return pos, 1 if packet_values[0] == packet_values[1] else 0

    binary_data = ''
    for char in hex_data:
        n = int(char, 16)
        binary_data += format(n, 'b').zfill(4)
    _, answer = read_packet(0)
    print(f'Answer for part 2: {answer}')

if __name__ == '__main__':
    input_data = parsing.file2data("../day16/input16.txt", lambda x : x.strip())[0]
    part1(input_data)
    part2(input_data)
