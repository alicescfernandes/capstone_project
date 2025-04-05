import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { API_BASE_URL } from '../constants';

export const quarterApi = createApi({
  reducerPath: 'quarterApi',
  baseQuery: fetchBaseQuery({ baseUrl: API_BASE_URL }),
  endpoints: (builder) => ({
    getQuarter: builder.query({
      query: (quarter) => ({
        url: 'quarters',
        params: { q: quarter ?? undefined },
      })
    }),
    
  }),
});

export const { useGetQuarterQuery, useChangeQuarterMutation } = quarterApi;
