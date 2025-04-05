import { Button, Spinner } from 'flowbite-react';
import { useGetQuarterQuery } from '../../api/endpoints';
import { useState } from 'react';

export function QuarterNavigation({ currentQuarter, setCurrentQuarter }) {

    const { data, isLoading, error } = useGetQuarterQuery(currentQuarter, {
        forceRefetch: true
    });

    if (isLoading) return <Spinner size="sm" aria-label="Info spinner example" className="me-3" light />
    if (error) return <p>Erro ao obter quarter</p>;


    const { quarter, isFirst, isLast } = data;

    function onQuarterChange(quarter) {
        setCurrentQuarter(quarter);
    }

    return (
        <div className="flex items-center justify-center gap-4">
            {!isFirst && (
                <Button
                    onClick={() => onQuarterChange(quarter.number - 1)}
                    color="gray"
                    outline
                    pill
                >
                    <svg
                        className="w-6 h-6 transition-colors duration-200 ease-in-out"
                        viewBox="0 0 24 24"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M5 12h14M5 12l4-4m-4 4 4 4"
                            stroke="currentColor"
                            strokeWidth="2"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                        />
                    </svg>
                    <span className="sr-only">Quarter anterior</span>
                </Button>
            )}

            <h1 className="text-2xl font-semibold text-gray-800 dark:text-white">
                Quarter {quarter.number}
            </h1>

            {!isLast && (
                <Button
                    onClick={() => onQuarterChange(quarter.number + 1)}
                    color="gray"
                    outline
                    pill
                >
                    <svg
                        className="w-6 h-6"
                        viewBox="0 0 24 24"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M19 12H5m14 0-4 4m4-4-4-4"
                            stroke="currentColor"
                            strokeWidth="2"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                        />
                    </svg>
                    <span className="sr-only">Quarter seguinte</span>
                </Button>
            )}
        </div>
    );
}
