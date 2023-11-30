package stringutil

import (
	"testing"
    "strings"
)

func ToUpper(s string) string {
	return strings.ToUpper(s)
}

func ToLower(s string) string {
	return strings.ToLower(s)
}

func Concat(a, b string) string {
	return a + b
}

func TestStringFunctions(t *testing.T) {
	testCases := []struct {
		name     string
		function func(string) string
		input    string
		expected string
	}{
		{
			name:     "Test ToUpper",
			function: ToUpper,
			input:    "hello",
			expected: "HELLO",
		},
		{
			name:     "Test ToLower",
			function: ToLower,
			input:    "WORLD",
			expected: "world",
		},
		{
			name:     "Test Concat",
			function: func(s string) string { return Concat(s, s) },
			input:    "Hi ",
			expected: "Hi Hi ",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := tc.function(tc.input)
			if result != tc.expected {
				t.Errorf("got %s, want %s", result, tc.expected)
			}
		})
	}
}
